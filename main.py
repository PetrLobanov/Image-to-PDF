from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

all_path_files = []


def files_convert():
    if (all_path_files):
        messagebox.showinfo('Path', 'Укажи путь куда будем сохранять PDF')
        directory = filedialog.askdirectory()

        rgb_list = []
        for image in all_path_files:
            img = Image.open(image)
            rgb = img.convert('RGB')
            rgb_list.append(rgb)

        convert = rgb_list[0]
        del rgb_list[0]

        convert.save(directory+'/document.pdf', save_all=True, append_images=rgb_list)
        messagebox.showinfo('Well', 'Документ готов)')

    else:
        messagebox.showinfo('Warning!', 'Нет выбраных изображений!')


def get_files():
    all_path_files.clear()
    files = filedialog.askopenfilenames(filetypes=[("Images", ".jpg .png .jpeg")])
    for i in range(len(files)):
        all_path_files.append(files[i])
        label = Label(text=files[i])
        label.grid(row=i+1, column=0)


def open_window():
    window = Tk()
    window.title('Img to PDF')
    x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
    y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
    window.wm_geometry("+%d+%d" % (x - 300, y - 150))
    window.geometry('800x400')

    #btn get files
    btn_files = Button(window, text='Выберите файлы', command=get_files, font=("Arial Bold", 20))
    btn_files.grid(column=0, row=0, padx=20, pady=20)

    #btn convert
    btn_convert = Button(window, text='Конвертировать', command=files_convert, font=("Arial Bold", 20))
    btn_convert.grid(column=1, row=0, padx=20, pady=20)

    window.mainloop()


if __name__ == '__main__':
    open_window()