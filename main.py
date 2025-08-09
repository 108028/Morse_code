function 接收 (文字: string) {
    握手包.push(文字)
    if (文字 == "#") {
        握手包 = []
        basic.clearScreen()
    }
    單播放(文字)
}
function 啟動結束 () {
    圖像列表 = [
    images.createImage(`
        . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # # .
        `),
    images.createImage(`
        . # # # .
        . # # # .
        . # # # .
        . . # . .
        . # # # .
        `),
    images.createImage(`
        # # # . .
        . . . # .
        # # . . #
        . . # . #
        # . # . #
        `),
    images.createImage(`
        # . # . #
        # . # . .
        # . . # #
        . # . . .
        . . # # #
        `),
    images.createImage(`
        . # . . .
        # # . # .
        # # . # .
        # # . # .
        . # . . .
        `),
    images.createImage(`
        . # # . .
        . # # # .
        . # # # .
        . # # # .
        . # # # .
        `)
    ]
    images.createBigImage(`
        . . . . . . . . . .
        . . . . . . . . . .
        # . # . # . # . . #
        . . . . . . . . . .
        . . . . . . . . . .
        `).scrollImage(1, 200)
    images.createBigImage(`
        . . . . # . . . . .
        . . . . # . . . . .
        . # . . # . . . . .
        . . . . . . . . . .
        . . . . # . . . . .
        `).scrollImage(1, 200)
    basic.showLeds(`
        . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # # .
        `)
}
function 讀取大小 (檔案: any[]) {
    while (true) {
        while (input.buttonIsPressed(Button.A)) {
            if (input.buttonIsPressed(Button.B)) {
                break;
            }
        }
        if (input.buttonIsPressed(Button.B)) {
            break;
        }
        if (檔案.length < 8) {
            basic.showString("" + 檔案.length + "BYTE")
        } else if (檔案.length / 8 < 1000) {
            basic.showString("" + Math.round(檔案.length / 8) + "KB")
        } else if (檔案.length / 8000 < 1000) {
            basic.showString("" + Math.round(檔案.length / 8000) + "MB")
        } else {
            basic.showString("" + Math.round(檔案.length / 80000000) + "GB")
        }
        break;
    }
}
function 單播放 (數據: string) {
    if (數據 == "1") {
        music.play(music.createSoundExpression(
        WaveShape.Sine,
        2000,
        2000,
        125,
        125,
        1,
        SoundExpressionEffect.None,
        InterpolationCurve.Linear
        ), music.PlaybackMode.InBackground)
        led.plotBrightness(2, 2, 255)
    } else {
        led.plotBrightness(2, 2, 100)
    }
}
function 摩斯密碼hi () {
    摩斯密碼 = []
    for (let index = 0; index < 5; index++) {
        摩斯密碼.push("0")
    }
    for (let index = 0; index < 4; index++) {
        for (let index = 0; index < 10; index++) {
            摩斯密碼.push("1")
        }
        for (let index = 0; index < 10; index++) {
            摩斯密碼.push("0")
        }
    }
    for (let index = 0; index < 4; index++) {
        摩斯密碼.push("0")
    }
    for (let index = 0; index < 2; index++) {
        for (let index = 0; index < 10; index++) {
            摩斯密碼.push("1")
        }
        for (let index = 0; index < 10; index++) {
            摩斯密碼.push("0")
        }
    }
}
input.onButtonPressed(Button.AB, function () {
    模式 += 1
    if (6 == 模式) {
        模式 = 0
    }
    圖像列表[模式].showImage(0)
})
radio.onReceivedString(function (receivedString) {
    if (模式 == 3) {
        if (receivedString == "##") {
            圖像列表[模式].showImage(0)
        } else {
            接收(receivedString)
        }
    }
})
function 錄製 () {
    if (input.buttonIsPressed(Button.B)) {
        while (input.buttonIsPressed(Button.B)) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                `)
            重設()
        }
        while (true) {
            if (input.buttonIsPressed(Button.A)) {
                摩斯密碼.push("1")
                led.plotBrightness(2, 2, 255)
                music.play(music.createSoundExpression(
                WaveShape.Sine,
                2000,
                2000,
                255,
                255,
                50,
                SoundExpressionEffect.None,
                InterpolationCurve.Linear
                ), music.PlaybackMode.InBackground)
            } else {
                摩斯密碼.push("0")
                led.plotBrightness(2, 2, 50)
            }
            if (input.buttonIsPressed(Button.B)) {
                basic.showIcon(IconNames.Yes)
                break;
            }
            basic.pause(50)
        }
        while (input.buttonIsPressed(Button.AB)) {
        	
        }
        basic.pause(100)
    }
    圖像列表[模式].showImage(0)
}
function 播放 () {
    if (input.buttonIsPressed(Button.A)) {
        while (input.buttonIsPressed(Button.A)) {
            basic.clearScreen()
            if (input.buttonIsPressed(Button.B)) {
                break;
            }
        }
        if (!(input.buttonIsPressed(Button.B))) {
            運算暫存 = 0
            basic.clearScreen()
            for (let index = 0; index < 摩斯密碼.length; index++) {
                if (摩斯密碼[運算暫存] == "1") {
                    music.play(music.createSoundExpression(
                    WaveShape.Sine,
                    2000,
                    2000,
                    255,
                    255,
                    50,
                    SoundExpressionEffect.None,
                    InterpolationCurve.Linear
                    ), music.PlaybackMode.InBackground)
                    led.plotBrightness(2, 2, 255)
                } else {
                    led.plotBrightness(2, 2, 50)
                }
                運算暫存 += 1
                basic.pause(50)
                if (input.buttonIsPressed(Button.B)) {
                    break;
                }
            }
            basic.pause(100)
            basic.clearScreen()
            圖像列表[模式].showImage(0)
        }
    }
}
function 播放握手包 () {
    while (true) {
        while (input.buttonIsPressed(Button.B)) {
            basic.clearScreen()
            if (input.buttonIsPressed(Button.A)) {
                break;
            }
        }
        if (input.buttonIsPressed(Button.A)) {
            break;
        }
        運算暫存 = 0
        basic.clearScreen()
        for (let index = 0; index < 握手包.length; index++) {
            if (握手包[運算暫存] == "1") {
                music.play(music.createSoundExpression(
                WaveShape.Sine,
                2000,
                2000,
                255,
                255,
                50,
                SoundExpressionEffect.None,
                InterpolationCurve.Linear
                ), music.PlaybackMode.InBackground)
                led.plotBrightness(2, 2, 255)
            } else {
                led.plotBrightness(2, 2, 50)
            }
            運算暫存 += 1
            basic.pause(50)
            if (input.buttonIsPressed(Button.A)) {
                break;
            }
        }
        basic.pause(100)
        basic.clearScreen()
        圖像列表[模式].showImage(0)
        break;
    }
}
function 發送 () {
    while (true) {
        while (input.buttonIsPressed(Button.A)) {
            if (input.buttonIsPressed(Button.B)) {
                break;
            }
        }
        if (input.buttonIsPressed(Button.B)) {
            break;
        }
        radio.sendString("#")
        if (!(input.buttonIsPressed(Button.A))) {
            運算暫存 = 0
            basic.clearScreen()
            for (let index = 0; index < 摩斯密碼.length; index++) {
                if (摩斯密碼[運算暫存] == "1") {
                    led.plotBrightness(2, 2, 255)
                    music.play(music.createSoundExpression(
                    WaveShape.Sine,
                    2000,
                    2000,
                    125,
                    125,
                    1,
                    SoundExpressionEffect.None,
                    InterpolationCurve.Linear
                    ), music.PlaybackMode.InBackground)
                    radio.sendString("1")
                } else {
                    led.plotBrightness(2, 2, 50)
                    radio.sendString("0")
                }
                運算暫存 += 1
                basic.pause(2)
                if (input.buttonIsPressed(Button.A)) {
                    break;
                }
            }
            basic.pause(100)
            basic.clearScreen()
            圖像列表[模式].showImage(0)
        }
        radio.sendString("##")
        break;
    }
}
function 重設 () {
    摩斯密碼 = [""]
}
let 運算暫存 = 0
let 摩斯密碼: string[] = []
let 圖像列表: Image[] = []
let 握手包: string[] = []
let 模式 = 0
radio.sendString("")
摩斯密碼hi()
模式 = 0
啟動結束()
basic.forever(function () {
    if (模式 == 1) {
        錄製()
    } else if (模式 == 4) {
        播放()
    } else if (模式 == 5) {
        if (input.buttonIsPressed(Button.A)) {
            讀取大小(摩斯密碼)
        }
        圖像列表[模式].showImage(0)
    } else if (模式 == 2) {
        if (input.buttonIsPressed(Button.A)) {
            發送()
        }
    } else if (模式 == 3) {
        if (input.buttonIsPressed(Button.B)) {
            播放握手包()
            圖像列表[模式].showImage(0)
        }
        if (input.buttonIsPressed(Button.A)) {
            images.createImage(`
                . # # . .
                . # # # .
                . # # # .
                . # # # .
                . # # # .
                `).scrollImage(1, 200)
            讀取大小(握手包)
            圖像列表[模式].showImage(0)
        }
    } else {
    	
    }
})
