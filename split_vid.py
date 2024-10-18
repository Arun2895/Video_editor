import gradio as gr
from moviepy.editor import VideoFileClip

# Function to separate audio and video
def separate_audio_video(video_path):
    try:
        # Load the video file from the path directly
        video_clip = VideoFileClip(video_path)
        
        # Define output paths for the separated files
        video_output_path = "output_video.mp4"
        audio_output_path = "output_audio.mp3"
        
        # Remove the audio and save the video without audio
        video_clip.without_audio().write_videofile(video_output_path, codec='libx264')
        
        # Extract the audio from the video and save it as an mp3 file
        video_clip.audio.write_audiofile(audio_output_path)
        
        # Close the video clip to release resources
        video_clip.close()
        
        # Return the paths of the video and audio for download
        return video_output_path, audio_output_path

    except Exception as e:
        # Return error message if something goes wrong
        return str(e), None

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Separate Audio and Video")

    # Upload video file input
    video_input = gr.Video(label="Upload a Video File")

    # Outputs for the separated video (without audio) and audio (mp3)
    video_output = gr.File(label="Download Video Without Audio")
    audio_output = gr.File(label="Download Extracted Audio (MP3)")

    # Button to trigger the separation process
    submit_button = gr.Button("Separate Audio and Video")

    # Connect the button with the function to process the video
    submit_button.click(separate_audio_video, inputs=video_input, outputs=[video_output, audio_output])

# Launch the Gradio interface
demo.launch()
