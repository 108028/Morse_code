def 接收(文字: str):
    global 握手包
    握手包.append(文字)
    if 文字 == "#":
        握手包 = []
        basic.clear_screen()
    單播放(文字)
def 啟動結束():
    global 圖像列表
    圖像列表 = [images.create_image("""
            . . # . .
            # . # . #
            # . # . #
            # . . . #
            . # # # .
            """),
        images.create_image("""
            . # # # .
            . # # # .
            . # # # .
            . . # . .
            . # # # .
            """),
        images.create_image("""
            # # # . .
            . . . # .
            # # . . #
            . . # . #
            # . # . #
            """),
        images.create_image("""
            # . # . #
            # . # . .
            # . . # #
            . # . . .
            . . # # #
            """),
        images.create_image("""
            . # . . .
            # # . # .
            # # . # .
            # # . # .
            . # . . .
            """),
        images.create_image("""
            . # # . .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            """),
        images.create_image("""
            . . . . .
            . . . . .
            # # # # #
            . . . . .
            . . . . .
            """)]
    images.create_big_image("""
        . . . . . . . . . .
        . . . . . . . . . .
        # . # . # . # . . #
        . . . . . . . . . .
        . . . . . . . . . .
        """).scroll_image(1, 200)
    images.create_big_image("""
        . . . . # . . . . .
        . . . . # . . . . .
        . # . . # . . . . .
        . . . . . . . . . .
        . . . . # . . . . .
        """).scroll_image(1, 200)
    basic.show_leds("""
        . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # # .
        """)
def 讀取大小(檔案: List[any]):
    while True:
        while input.button_is_pressed(Button.A):
            if input.button_is_pressed(Button.B):
                break
        if input.button_is_pressed(Button.B):
            break
        if len(檔案) < 8:
            basic.show_string("" + str(len(檔案)) + "BYTE")
        elif len(檔案) / 8 < 1000:
            basic.show_string("" + str(Math.round(len(檔案) / 8)) + "KB")
        elif len(檔案) / 8000 < 1000:
            basic.show_string("" + str(Math.round(len(檔案) / 8000)) + "MB")
        else:
            basic.show_string("" + str(Math.round(len(檔案) / 80000000)) + "GB")
        break

def on_button_pressed_ab():
    global 模式
    模式 += 1
    if 7 == 模式:
        模式 = 0
    圖像列表[模式].show_image(0)
    radio.send_number(2)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def 單播放(數據: str):
    if 數據 == "1":
        led.plot_brightness(2, 2, 255)
        音樂(2000, 1, 125, V2)
    else:
        led.plot_brightness(2, 2, 100)

def on_received_string(receivedString):
    if 模式 == 3:
        if receivedString == "##":
            圖像列表[模式].show_image(0)
        else:
            接收(receivedString)
radio.on_received_string(on_received_string)

def 音樂(起始: number, 時長: number, 響度: number, V2: bool):
    if V2:
        music.play(music.create_sound_expression(WaveShape.SINE,
                起始,
                起始,
                響度,
                響度,
                時長,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.IN_BACKGROUND)
    else:
        music.set_tempo(60)
        music.play(music.tone_playable(784, 時長 / 1000),
            music.PlaybackMode.IN_BACKGROUND)
def 摩斯密碼hi():
    global 摩斯密碼
    摩斯密碼 = []
    for index in range(5):
        摩斯密碼.append("0")
    for index2 in range(4):
        for index3 in range(10):
            摩斯密碼.append("1")
        for index4 in range(10):
            摩斯密碼.append("0")
    for index5 in range(4):
        摩斯密碼.append("0")
    for index6 in range(2):
        for index7 in range(10):
            摩斯密碼.append("1")
        for index8 in range(10):
            摩斯密碼.append("0")
def 錄製():
    if input.button_is_pressed(Button.B):
        basic.pause(50)
        if not (input.button_is_pressed(Button.A)):
            while input.button_is_pressed(Button.B):
                basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)
                重設()
            while True:
                if input.button_is_pressed(Button.A):
                    音樂(2000, 50, 255, V2)
                    摩斯密碼.append("1")
                    led.plot_brightness(2, 2, 255)
                else:
                    摩斯密碼.append("0")
                    led.plot_brightness(2, 2, 50)
                if input.button_is_pressed(Button.B):
                    basic.show_icon(IconNames.YES)
                    break
                basic.pause(50)
            while input.button_is_pressed(Button.AB):
                pass
            basic.pause(100)
    圖像列表[模式].show_image(0)
def 播放():
    global 運算暫存
    if input.button_is_pressed(Button.A):
        basic.pause(50)
        if not (input.button_is_pressed(Button.B)):
            while input.button_is_pressed(Button.A):
                basic.clear_screen()
                basic.pause(50)
                if input.button_is_pressed(Button.B):
                    break
            if not (input.button_is_pressed(Button.B)):
                運算暫存 = 0
                basic.clear_screen()
                for index9 in range(len(摩斯密碼)):
                    if 摩斯密碼[運算暫存] == "1":
                        音樂(2000, 50, 255, V2)
                        led.plot_brightness(2, 2, 255)
                    else:
                        led.plot_brightness(2, 2, 50)
                    運算暫存 += 1
                    basic.pause(50)
                    if input.button_is_pressed(Button.B):
                        break
                basic.pause(100)
                basic.clear_screen()
                圖像列表[模式].show_image(0)
def 播放握手包():
    global 運算暫存
    while True:
        while input.button_is_pressed(Button.B):
            basic.clear_screen()
            if input.button_is_pressed(Button.A):
                break
        if input.button_is_pressed(Button.A):
            break
        運算暫存 = 0
        basic.clear_screen()
        for index10 in range(len(握手包)):
            if 握手包[運算暫存] == "1":
                音樂(2000, 50, 255, V2)
                led.plot_brightness(2, 2, 255)
            else:
                led.plot_brightness(2, 2, 50)
            運算暫存 += 1
            basic.pause(50)
            if input.button_is_pressed(Button.A):
                break
        basic.pause(100)
        basic.clear_screen()
        圖像列表[模式].show_image(0)
        break
def 發送():
    global 運算暫存
    while True:
        while input.button_is_pressed(Button.A):
            if input.button_is_pressed(Button.B):
                break
        if input.button_is_pressed(Button.B):
            break
        radio.send_string("#")
        if not (input.button_is_pressed(Button.A)):
            運算暫存 = 0
            basic.clear_screen()
            for index11 in range(len(摩斯密碼)):
                if 摩斯密碼[運算暫存] == "1":
                    led.plot_brightness(2, 2, 255)
                    音樂(2000, 1, 125, V2)
                    radio.send_string("1")
                else:
                    led.plot_brightness(2, 2, 50)
                    radio.send_string("0")
                運算暫存 += 1
                basic.pause(2)
                if input.button_is_pressed(Button.B):
                    break
            basic.clear_screen()
            圖像列表[模式].show_image(0)
        radio.send_string("##")
        break
def 重設():
    global 摩斯密碼
    摩斯密碼 = [""]

def on_received_number(receivedNumber):
    if 模式 == 6:
        if receivedNumber == 1:
            音樂(2000, 3, 255, V2)
            led.plot_brightness(2, 0, 255)
        elif receivedNumber == 0:
            led.plot_brightness(2, 0, 50)
        else:
            led.plot_brightness(2, 0, 0)
radio.on_received_number(on_received_number)

運算暫存 = 0
摩斯密碼: List[str] = []
圖像列表: List[Image] = []
握手包: List[str] = []
模式 = 0
V22 = False
V2 = True
radio.send_string("")
摩斯密碼hi()
模式 = 0
啟動結束()

def on_forever():
    if 模式 == 1:
        錄製()
    elif 模式 == 4:
        播放()
    elif 模式 == 5:
        if input.button_is_pressed(Button.A):
            讀取大小(摩斯密碼)
        圖像列表[模式].show_image(0)
    elif 模式 == 2:
        if input.button_is_pressed(Button.A):
            發送()
    elif 模式 == 3:
        if input.button_is_pressed(Button.B):
            basic.pause(50)
            if input.button_is_pressed(Button.B):
                播放握手包()
                圖像列表[模式].show_image(0)
        if input.button_is_pressed(Button.A):
            basic.pause(50)
            if input.button_is_pressed(Button.A):
                images.create_image("""
                    . # # . .
                    . # # # .
                    . # # # .
                    . # # # .
                    . # # # .
                    """).scroll_image(1, 200)
                讀取大小(握手包)
                圖像列表[模式].show_image(0)
    elif 模式 == 6:
        if input.button_is_pressed(Button.A):
            radio.send_number(1)
            led.plot_brightness(2, 4, 255)
        else:
            radio.send_number(0)
            led.plot_brightness(2, 4, 50)
    else:
        pass
basic.forever(on_forever)
