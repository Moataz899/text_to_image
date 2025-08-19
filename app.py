from flask import Flask, render_template, request, send_file, jsonify
from io import BytesIO
import base64
import os
import random
from models.model1 import generate_image_fast

app = Flask(__name__)

# Add favicon route
@app.route('/favicon.ico')
def favicon():
    return send_file('static/favicon.ico', mimetype='image/x-icon')

# Flask Routes
@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    image_data = None
    
    if request.method == "POST":
        prompt = request.form.get("prompt")
        if not prompt or not prompt.strip():
            error = "Please enter a prompt."
        else:
            # Use enhanced generation with better parameters
            seed = random.randint(1, 1000000)  # Random seed for variety
            img, err = generate_image_fast(
                prompt, 
                steps=30,  # Increased steps for better quality
                guidance=7.5, 
                seed=seed
            )
            if err:
                error = err
            else:
                # Convert image to base64 for display in HTML
                buf = BytesIO()
                img.save(buf, format="PNG")
                image_data = base64.b64encode(buf.getvalue()).decode("utf-8")
                
    return render_template("index.html", error=error, image_data=image_data)

@app.route("/generate", methods=["POST"])
def generate_api():
    """API endpoint for image generation"""
    data = request.get_json()
    prompt = data.get("prompt", "")
    steps = data.get("steps", 30)
    guidance = data.get("guidance", 7.5)
    seed = data.get("seed", None)
    
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    img, err = generate_image_fast(prompt, steps=steps, guidance=guidance, seed=seed)
    if err:
        return jsonify({"error": err}), 500
    
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    
    return jsonify({
        "image": base64.b64encode(buf.getvalue()).decode("utf-8"),
        "prompt": prompt,
        "steps": steps,
        "guidance": guidance,
        "seed": seed
    })

@app.route("/download")
def download_image():
    prompt = request.args.get("prompt")
    steps = int(request.args.get("steps", 30))
    guidance = float(request.args.get("guidance", 7.5))
    seed = int(request.args.get("seed", random.randint(1, 1000000)))
    
    img, err = generate_image_fast(prompt, steps=steps, guidance=guidance, seed=seed)
    if err:
        return jsonify({"error": err}), 500
    
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png", as_attachment=True, download_name=f"generated_image_{seed}.png")

if __name__ == "__main__":
    app.run(debug=True)
