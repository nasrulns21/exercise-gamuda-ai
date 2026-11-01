# Week 8 - Multimodal Image and Video Analytics

## Completed exercises

- `01-image-analytics`: responsive image upload UI with a customisable multimodal prompt.
- `02-video-analytics`: detailed, bullet, time-coded, and quiz-with-answer-key prompt modes.

Live multimodal calls require the user's own `GEMINI_API_KEY` and are an external verification checkpoint. Deterministic prompt tests need no key.

## Original student work

`exercise_1/video_analytics.py` uses OpenCV to capture webcam video, apply background subtraction, and draw a box around detected motion.

Install OpenCV and run the script:

```bash
pip install opencv-python
python exercise_1/video_analytics.py
```

Press `Q` to close the video window.
