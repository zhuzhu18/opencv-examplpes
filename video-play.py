import cv2

cap = cv2.VideoCapture('/home/zhuzhu/视频/vlc-record-2019-05-22-19h01m58s-AlphaPose_together.avi-.mp4')

while True:
  ret, frame = cap.read()
  cv2.imshow('frame', frame)
  if cv2.waitKey(30) & 0xFF == ord('q'):
    break
