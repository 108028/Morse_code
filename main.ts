input.onButtonPressed(Button.AB, function () {
    模式 += 1
    if (5 == 模式) {
        模式 = 0
    }
    圖像列表[模式].showImage(0)
})
function 重設 () {
    摩斯密碼 = [""]
}
let 運算暫存 = 0
let 摩斯密碼: string[] = []
let 圖像列表: Image[] = []
let 模式 = 0
模式 = 0
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
basic.forever(function () {
    if (模式 == 1) {
        if (input.buttonIsPressed(Button.A)) {
            摩斯密碼.unshift("1")
        } else {
            摩斯密碼.unshift("0")
        }
    } else if (模式 == 4) {
        if (input.buttonIsPressed(Button.A)) {
            運算暫存 = 0
            for (let index = 0; index < 摩斯密碼.length; index++) {
                if (摩斯密碼[運算暫存] == "1") {
                    music.play(music.createSoundExpression(
                    WaveShape.Sine,
                    2000,
                    2000,
                    255,
                    255,
                    10,
                    SoundExpressionEffect.None,
                    InterpolationCurve.Linear
                    ), music.PlaybackMode.UntilDone)
                } else {
                    music.play(music.createSoundExpression(
                    WaveShape.Sine,
                    1,
                    1,
                    0,
                    0,
                    10,
                    SoundExpressionEffect.None,
                    InterpolationCurve.Linear
                    ), music.PlaybackMode.UntilDone)
                }
                運算暫存 += 1
            }
        }
    } else {
    	
    }
})
