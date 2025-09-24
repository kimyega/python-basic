from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from wand.image import *


# ## 함수 정의 부분 ##
# 프로그램이 시작될 때 모든 함수를 먼저 읽을 수 있도록 상단에 배치합니다.

def displayImage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY

    window.geometry(str(width) + "x" + str(height))
    if canvas != None:
        canvas.destroy()

    canvas = Canvas(window, width=width, height=height)
    paper = PhotoImage(width=width, height=height)
    canvas.create_image((width / 2, height / 2), image=paper, state="normal")

    blob = img.make_blob(format='RGB')

    # [FIXED] 반복문 순서를 (세로 -> 가로)로 수정
    for i in range(0, height):
        for k in range(0, width):
            r = blob[(i * width + k) * 3 + 0]
            g = blob[(i * width + k) * 3 + 1]
            b = blob[(i * width + k) * 3 + 2]
            paper.put("#%02x%02x%02x" % (r, g, b), (k, i))
    canvas.pack()


def func_open():
    global window, canvas, paper, photo, photo2, oriX, oriY

    # [FIXED] askopenfile -> askopenfilename으로 변경하여 파일 경로를 문자열로 받음
    readFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일",
                                                        "*.jpg; *.jpeg; *.bmp; *.png; *.tif; *.gif"), ("모든 파일", "*.*")))

    # 사용자가 파일 선택을 취소한 경우를 대비
    if not readFp:
        return

    photo = Image(filename=readFp)
    oriX = photo.width
    oriY = photo.height

    photo2 = photo.clone()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_save():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None:
        return
    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg",
                           filetypes=(("jpg 파일", "*.jpg; *.jpeg"), ("모든 파일", "*.*")))

    if not saveFp:
        return

    savePhoto = photo2.convert("jpg")
    savePhoto.save(filename=saveFp.name)


def func_exit():
    window.quit()
    window.destroy()


def func_zoomin():
    global photo, photo2
    if photo2 is None: return
    scale = askinteger("확대", "확대할 배율을 입력하세요", minvalue=2, maxvalue=4)
    if scale is None: return
    photo2 = photo.clone()
    photo2.resize(int(oriX * scale), int(oriY * scale))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_zoomout():
    global photo, photo2
    if photo2 is None: return
    scale = askinteger("축소", "축소할 배율을 입력하세요", minvalue=2, maxvalue=4)
    if scale is None: return
    photo2 = photo.clone()
    photo2.resize(int(oriX / scale), int(oriY / scale))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_mirror1():  # 상하 반전
    global photo, photo2
    if photo2 is None: return
    photo2 = photo.clone()
    photo2.flip()  # [FIXED] 상하 반전은 flip()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_mirror2():  # 좌우 반전
    global photo, photo2
    if photo2 is None: return
    photo2 = photo.clone()
    photo2.flop()  # 좌우 반전은 flop()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_rotate():
    global photo, photo2
    if photo2 is None: return
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)
    if degree is None: return
    photo2 = photo.clone()
    photo2.rotate(degree)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_bright():
    global photo, photo2
    if photo2 is None: return
    value = askinteger("밝게", "값을 입력하세요(100-200)", minvalue=100, maxvalue=200)
    if value is None: return
    photo2 = photo.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_dark():
    global photo, photo2
    if photo2 is None: return
    value = askinteger("어둡게", "값을 입력하세요(0-100)", minvalue=0, maxvalue=100)
    if value is None: return
    photo2 = photo.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_clear():
    global photo, photo2
    if photo2 is None: return
    value = askinteger("선명하게", "값을 입력하세요(100-200)", minvalue=100, maxvalue=200)
    if value is None: return
    # 선명하게는 채도(saturation)를 조절해야 합니다.
    photo2 = photo.clone()
    photo2.modulate(100, value, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_unclear():
    global photo, photo2
    if photo2 is None: return
    value = askinteger("탁하게", "값을 입력하세요(0-100)", minvalue=0, maxvalue=100)
    if value is None: return
    # 탁하게는 채도(saturation)를 조절해야 합니다.
    photo2 = photo.clone()
    photo2.modulate(100, value, 100)
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


def func_bw():
    global photo, photo2
    if photo2 is None: return
    photo2 = photo.clone()
    photo2.type = "grayscale"  # 오타 수정: greyscale -> grayscale
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)


# ## 전역 변수 선언 ##
window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0

# ## 메인 코드 부분 ##
window = Tk()
window.geometry("250x250")
window.title("미니 포토샵")

mainMenu = Menu(window)
window.config(menu=mainMenu)

# 빈 이미지를 표시하기보다 처음엔 레이블을 비워두는 것이 더 깔끔합니다.
pLabel = Label(window)
pLabel.pack(expand=1, anchor=CENTER)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_command(label="파일 저장", command=func_save)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(1)", menu=image1Menu)
image1Menu.add_command(label="확대", command=func_zoomin)
image1Menu.add_command(label="축소", command=func_zoomout)
image1Menu.add_separator()
image1Menu.add_command(label="상하 반전", command=func_mirror1)
image1Menu.add_command(label="좌우 반전", command=func_mirror2)
image1Menu.add_command(label="회전", command=func_rotate)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(2)", menu=image2Menu)
image2Menu.add_command(label="밝게", command=func_bright)
image2Menu.add_command(label="어둡게", command=func_dark)
image2Menu.add_separator()
image2Menu.add_command(label="선명하게", command=func_clear)
# 메뉴의 '탁하게'가 func_dark로 잘못 연결되어 있던 것을 수정
image2Menu.add_command(label="탁하게", command=func_unclear)
image2Menu.add_separator()
image2Menu.add_command(label="흑백이미지", command=func_bw)

# [FIXED] window.mainloop()는 항상 코드의 맨 마지막에 위치해야 합니다.
window.mainloop()