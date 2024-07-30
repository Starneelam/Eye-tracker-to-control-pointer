import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    _, body = cam.read()
    body = cv2.flip(body, 1)
    rgb_body = cv2.cvtColor(body, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_body)
    landmark_points = output.multi_face_landmarks
    body_h, body_w, _ = body.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * body_w)
            y = int(landmark.y * body_h)
            cv2.circle(body, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * body_w)
            y = int(landmark.y * body_h)
            cv2.circle(body, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye tracker- Controlled Mouse', body)
    cv2.waitKey(1)
