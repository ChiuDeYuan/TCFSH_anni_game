
from PIL import Image,ImageTk
import PySimpleGUI as sg
import __conv
import numpy as np

kernel = [np.array([[1]]),
          np.array([[1,1,1],[1,-7,1],[1,1,1]]),
          np.array([[0,1,1,2,2,2,1,1,0],[1,2,4,5,5,5,4,2,1],[1,4,5,3,0,3,5,4,1],[2,5,3,-12,-24,-12,3,5,2],[2,5,0,-24,-40,-24,0,5,2],[2,5,3,-12,-24,-12,3,5,2],[1,4,5,3,0,3,4,4,1],[1,2,4,5,5,5,4,2,1],[0,1,1,2,2,2,1,1,0]]),
          np.array([[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[-1,-1,-1,-1,-1]]),
          np.array([[1]]),
          ]
kernel_now = 0
gray_switch = False

############## GUI ################
sg.theme('LightGreen')
layout = [
        [sg.Push(),
         sg.Text('卷積處理圖片', size=(20, 2), justification='c', font=64),
         sg.Push()],
        [sg.Push(),sg.Push(),sg.Push(),
         sg.Image(key="-IMAGE-",size=(400,600),),
         sg.Push(),
         sg.Image(key="-IMAGE2-",size=(400,600),),
         sg.Push(),sg.Push(),sg.Push(),],
        [sg.Text('', size=(10,2))],
        [sg.Push(),
          sg.Text('卷積核 :', font=32),
          sg.Radio('原圖', 'kernel', enable_events=True, key='ori', default=True, font=32),
          sg.Radio('1', 'kernel', enable_events=True, key='k1', font=32),
          sg.Radio('2', 'kernel', enable_events=True, key='k2', font=32),
          sg.Radio('3', 'kernel', enable_events=True, key='k3', font=32),
          sg.Radio('自定義5X5', 'kernel', enable_events=True, key='k4', font=32),
          sg.Radio('自定義3X3', 'kernel', enable_events=True, key='k5', font=32),
          sg.Push(),],
        [sg.Push(),
         sg.Text('灰階 :', font=32),
          sg.Radio('Yes', 'gray', enable_events=True, key='gray_true', font=32),
          sg.Radio('No', 'gray', enable_events=True, key='gray_false', default=True, font=32),
          sg.Push(),],
        [sg.FileBrowse("Choose Image",target='-GETFILE-',key='-GETFILE-',
         enable_events=True,size=(15,2), font=32),
         sg.Text('',k='-TEXT1-'),],
    ]

#window = sg.Window('Convolution', layout)
window = sg.Window('Convolution', layout).Finalize()
window.Maximize()
#################################################

############## Customize Kernel #################
def str_to_int(tar):
    if tar == '':
        return 1
    elif '/' in tar:
        tar = tar.split('/')
        if(tar[1]==''):
            tar[1] = '1'
        try:
            return float(int(tar[0])/int(tar[1]))
        except:
            return 1
    else:
        try:
            return int(tar)
        except:
            return 1

def design_kernel_5X5():
    l1 = sg.Text('自訂kernel!!!', key='-OUT-', font=('Arial Bold', 16), expand_x=True, justification='center', size=(10, 2))
    t1 = sg.Input('', key='-INPUT1-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t2 = sg.Input('', key='-INPUT2-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t3 = sg.Input('', key='-INPUT3-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t4 = sg.Input('', key='-INPUT4-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t5 = sg.Input('', key='-INPUT5-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t6 = sg.Input('', key='-INPUT6-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t7 = sg.Input('', key='-INPUT7-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t8 = sg.Input('', key='-INPUT8-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t9 = sg.Input('', key='-INPUT9-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t10 = sg.Input('', key='-INPUT10-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t11 = sg.Input('', key='-INPUT11-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t12 = sg.Input('', key='-INPUT12-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t13 = sg.Input('', key='-INPUT13-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t14 = sg.Input('', key='-INPUT14-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t15 = sg.Input('', key='-INPUT15-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t16 = sg.Input('', key='-INPUT16-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t17 = sg.Input('', key='-INPUT17-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t18 = sg.Input('', key='-INPUT18-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t19 = sg.Input('', key='-INPUT19-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t20 = sg.Input('', key='-INPUT20-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t21 = sg.Input('', key='-INPUT21-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t22 = sg.Input('', key='-INPUT22-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t23 = sg.Input('', key='-INPUT23-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t24 = sg.Input('', key='-INPUT24-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t25 = sg.Input('', key='-INPUT25-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    b1 = sg.Button('Ok',  enable_events=True, key='-OK-', font=('Arial', 16), size=(5,1))
    b2 = sg.Button('Exit', font=('Arial', 16), size=(5,1))

    layout = [[l1], 
    [t1,t2,t3,t4,t5],
    [t6,t7,t8,t9,t10],
    [t11,t12,t13,t14,t15],
    [t16,t17,t18,t19,t20],
    [t21,t22,t23,t24,t25], 
    [sg.Text(' ')],
    [sg.Push(), b1, sg.Push(),b2,sg.Push()]]

    custo_kernel = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

    window = sg.Window('Design a kernel', layout, size=(300, 350))
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            custo_kernel = [[1]]
            break

        if event == '-OK-':
            for i in range(5):
                tmp=i*5
                for j in range(5):
                    input_key = '-INPUT'+str(tmp+j+1)+'-'
                    custo_kernel[i][j] = str_to_int(values[input_key])

            if custo_kernel==[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]:
                custo_kernel = [[1]]
            break
        
    window.close()
    kernel[4] = np.array(custo_kernel)

def design_kernel_3X3():
    l1 = sg.Text('自訂kernel!!!', key='-OUT-', font=('Arial Bold', 16), expand_x=True, justification='center', size=(10, 2))
    t1 = sg.Input('', key='-INPUT1-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t2 = sg.Input('', key='-INPUT2-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t3 = sg.Input('', key='-INPUT3-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t4 = sg.Input('', key='-INPUT4-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t5 = sg.Input('', key='-INPUT5-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t6 = sg.Input('', key='-INPUT6-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t7 = sg.Input('', key='-INPUT7-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t8 = sg.Input('', key='-INPUT8-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    t9 = sg.Input('', key='-INPUT9-', font=('Arial Bold', 20), expand_x=True, justification='left', size=(1, 2))
    b1 = sg.Button('Ok',  enable_events=True, key='-OK-', font=('Arial', 16), size=(5,1))
    b2 = sg.Button('Exit', font=('Arial', 16), size=(5,1))

    layout = [[l1], 
    [t1,t2,t3],
    [t4,t5,t6],
    [t7,t8,t9],
    [sg.Text(' ')],
    [sg.Push(), b1, sg.Push(),b2,sg.Push()]]

    custo_kernel = [[1,1,1],[1,1,1],[1,1,1]]

    window = sg.Window('Design a kernel', layout, size=(200, 300))
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            custo_kernel = [[1]]
            break

        if event == '-OK-':
            for i in range(3):
                tmp=i*3
                for j in range(3):
                    input_key = '-INPUT'+str(tmp+j+1)+'-'
                    custo_kernel[i][j] = str_to_int(values[input_key])

            if custo_kernel==[[1,1,1],[1,1,1],[1,1,1]]:
                custo_kernel = [[1]]
            break
        
    window.close()
    kernel[4] = np.array(custo_kernel)
#################################################

################ Resize Image ###################
def resize(image_file, new_size):
    im = Image.open(image_file)
    im.thumbnail(new_size, Image.Resampling.BILINEAR)
    try:
        im.save('./temp_img/tmp.jpg')
        return "./temp_img/tmp.jpg"
    except:
        im.save('./temp_img/tmp.png')
        return "./temp_img/tmp.png"

size = (400, 600)
#################################################

################ Update Image ###################
def update_img(idx, is_gray):
    result_path = __conv.conv(kernel[idx], targe_path, is_gray)
    result = Image.open(result_path)
    convolved_img = ImageTk.PhotoImage(result)
    window['-IMAGE2-'].update(data=convolved_img)
    window['-IMAGE2-'].set_size(window['-IMAGE2-'].get_size())
#################################################

#################### Work #######################
while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    if event == '-GETFILE-':

        targe_path = values['-GETFILE-']
        window['-TEXT1-'].update(targe_path)

        targe_path = resize(targe_path, size)
        image = Image.open(targe_path)
        photo_img = ImageTk.PhotoImage(image)
        
        window['-IMAGE-'].update(data=photo_img)
        window['-IMAGE-'].set_size(window['-IMAGE-'].get_size())

        window['ori'].update(value=True)
        window['gray_false'].update(value=True)
        values['ori'] = True
        values['k1'] = False
        values['k2'] = False
        values['k3'] = False
        values['k4'] = False
        values['gray_false'] = True
        values['gray_true'] = False
        gray_switch = False
        kernel_now = 0
        update_img(0, False)
    
    if (values['ori'] == True) and  (kernel_now != 0) :
        kernel_now = 0
        update_img(0, gray_switch)

    if (values['k1'] == True) and (kernel_now != 1):
        kernel_now = 1
        update_img(1, gray_switch)

    if (values['k2'] == True) and (kernel_now != 2):
        kernel_now = 2
        update_img(2, gray_switch)

    if (values['k3'] == True) and (kernel_now != 3):
        kernel_now = 3
        update_img(3, gray_switch)
    
    if (values['k4'] == True) and  (kernel_now != 4):
        kernel_now = 4
        design_kernel_5X5()
        update_img(4, gray_switch)

    if (values['k5'] == True) and  (kernel_now != 5):
        kernel_now = 5
        design_kernel_3X3()
        update_img(4, gray_switch)

    if (values['gray_true'] == True) and (gray_switch != True):
        gray_switch = True
        update_img(kernel_now, gray_switch)
    
    if (values['gray_false'] == True) and (gray_switch != False):
        gray_switch = False
        update_img(kernel_now, gray_switch)

window.close()
#################################################