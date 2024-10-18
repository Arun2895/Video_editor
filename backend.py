from flask import Flask, render_template, request, jsonify, redirect, url_for
import gradio as gr
import threading

app = Flask(__name__)

# Function 1: Merge Video (Mock)
def merge_video(video1, video2):
    # Replace with your actual logic
    return "Video merged successfully."

# Function 2: Increase Resolution (Mock)
def increase_resolution(video):
    # Replace with your actual logic
    return "Resolution increased successfully."

# Function 3: Split Video and Audio (Mock)
def split_audio_video(video):
    # Replace with your actual logic
    return "Audio and video split successfully."

# Function 4: Trim Video (Mock)
def trim_video(video, start_time, end_time):
    # Replace with your actual logic
    return "Video trimmed successfully."

# Gradio Interfaces
def launch_gradio_interfaces():
    # Gradio interface for merging videos
    merge_interface = gr.Interface(fn=merge_video,
                                    inputs=["video", "video"],
                                    outputs="text",
                                    title="Merge Video")
    
    increase_resolution_interface = gr.Interface(fn=increase_resolution,
                                                  inputs="video",
                                                  outputs="text",
                                                  title="Increase Resolution")
    
    split_audio_interface = gr.Interface(fn=split_audio_video,
                                          inputs="video",
                                          outputs="text",
                                          title="Split Audio and Video")

    trim_interface = gr.Interface(fn=trim_video,
                                   inputs=["video", "number", "number"],
                                   outputs="text",
                                   title="Trim Video")
    
    return {
        "merge": merge_interface,
        "increase_resolution": increase_resolution_interface,
        "split_audio": split_audio_interface,
        "trim": trim_interface,
    }

# Route to serve the main.html file
@app.route('/')
def index():
    return render_template('main.html')

@app.route('/merge_video')
def merge_video_page():
    interfaces = launch_gradio_interfaces()
    threading.Thread(target=interfaces["merge"].launch, kwargs={"share": True}).start()
    print("Merge Video interface launched")  # Add this line
    return redirect('/')

@app.route('/increase_resolution')
def increase_resolution_page():
    interfaces = launch_gradio_interfaces()
    threading.Thread(target=interfaces["increase_resolution"].launch, kwargs={"share": True}).start()
    return redirect('/')

@app.route('/split_audio_video')
def split_audio_video_page():
    interfaces = launch_gradio_interfaces()
    threading.Thread(target=interfaces["split_audio"].launch, kwargs={"share": True}).start()
    return redirect('/')

@app.route('/trim_video')
def trim_video_page():
    interfaces = launch_gradio_interfaces()
    threading.Thread(target=interfaces["trim"].launch, kwargs={"share": True}).start()
    return redirect('/')

# Route to handle function application
@app.route('/apply-function', methods=['POST'])
def apply_function():
    data = request.get_json()
    func = data['function']

    # Redirect based on the function chosen
    if func == 'merge video':
        return redirect(url_for('merge_video_page'))
    elif func == 'increase resolution':
        return redirect(url_for('increase_resolution_page'))
    elif func == 'split audio video':
        return redirect(url_for('split_audio_video_page'))
    elif func == 'video trim':
        return redirect(url_for('trim_video_page'))
    else:
        return jsonify({'result': 'Invalid function.'})

if __name__ == "__main__":
    app.run(debug=True)
