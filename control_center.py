from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter import messagebox
from image_processor import ImageProcessor


class ControlCenter:

    def __init__(self):
        self.processor = ImageProcessor()
        self.img_path = None
        self.img_name = None
        self.crt_path = None
        self.xaxis = 0
        self.yaxis = 0

        self.window = Tk()
        self.window.title("Image Watermark Processor")
        self.window.resizable(False, False)
        self.window.geometry("650x600")

        self.bg_img = PhotoImage(file="space.png")
        self.background = Label(self.window, image=self.bg_img)
        self.background.place(x=0, y=0)

        self.input_image = PhotoImage(file="logo.png")
        self.target_image = Label(self.window, image=self.input_image)
        self.target_image.place(x=50, y=10)

        self.open_button = Button(width=10, text="Open File", highlightthickness=0, command=self.open_file)
        self.open_button.place(x=400, y=400)

        self.text_label = Label(self.window, width=19, highlightthickness=0, text="Enter Watermark Text Here:")
        self.text_label.place(x=100, y=375)

        self.text_entry = Entry(width=19, highlightthickness=0)
        self.text_entry.place(x=100, y=400)

        self.text_button = Button(width=12, text="Save Text Watermark", highlightthickness=0, command=self.process_text_watermark)
        self.text_button.place(x=400, y=475)

        self.photo_button = Button(width=13, text="Save Photo Watermark", highlightthickness=0, command=self.process_photo_watermark)
        self.photo_button.place(x=400, y=550)

        self.size_label = Label(self.window, width=7, highlightthickness=0, text="Size:", anchor="w")
        self.size_label.place(x=100, y=450)

        self.var_size = StringVar()
        self.size = ttk.Combobox(self.window, width=5, textvariable=self.var_size)
        self.size["values"] = (20, 25, 30, 35, 40, 45, 50, 55, 60)
        self.size.place(x=100, y=475)
        self.size.current(0)

        self.color_label = Label(self.window, width=7, highlightthickness=0, text="Color:", anchor="w")
        self.color_label.place(x=175, y=450)

        self.var_color = StringVar()
        self.color = ttk.Combobox(self.window, width=5, textvariable=self.var_color)
        self.color["values"] = ("White", "Black", "Yellow", "Orange", "Blue", "Red", "Green", "Pink", "Purple")
        self.color.place(x=175, y=475)
        self.color.current(0)

        self.transparency_label = Label(self.window, width=12, highlightthickness=0, text="Transparency:", anchor="w")
        self.transparency_label.place(x=250, y=450)

        self.var_transparency = StringVar()
        self.transparency = ttk.Combobox(self.window, width=10, textvariable=self.var_transparency)
        self.transparency["values"] = (50, 100, 150, 200, 255)
        self.transparency.place(x=250, y=475)
        self.transparency.current(0)

        self.xaxis_label = Label(self.window, width=5, highlightthickness=0, text="X-Axis:", anchor="w")
        self.xaxis_label.place(x=100, y=525)

        self.xaxis_entry = Entry(width=5, highlightthickness=0)
        self.xaxis_entry.insert(0, 0)
        self.xaxis_entry.place(x=100, y=550)

        self.yaxis_label = Label(self.window, width=5, highlightthickness=0, text="Y-Axis:", anchor="w")
        self.yaxis_label.place(x=155, y=525)

        self.yaxis_entry = Entry(width=5, highlightthickness=0)
        self.yaxis_entry.insert(0, 0)
        self.yaxis_entry.place(x=155, y=550)

        self.yaxis_label = Label(self.window, width=16, highlightthickness=0, text="Watermark Photo Size:", anchor="w")
        self.yaxis_label.place(x=220, y=525)

        self.var_wmsize = StringVar()
        self.wmsize = ttk.Combobox(self.window, width=14, textvariable=self.var_wmsize)
        self.wmsize["values"] = ("10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%")
        self.wmsize.place(x=220, y=550)
        self.wmsize.current(0)

        self.window.mainloop()

    def file_normalization(self):
        self.crt_path = self.img_path.split(".")[0] + ".png"
        self.processor.resize_image(self.img_path, self.crt_path, 550, 350)

    def open_file(self):
        self.img_path = fd.askopenfilename()
        self.img_name = self.img_path.split("/")[-1].split(".")[0]

        self.file_normalization()
        self.input_image = PhotoImage(file=self.crt_path)
        self.target_image = Label(self.window, image=self.input_image)
        self.target_image.place(x=50, y=10)

    def process_text_watermark(self):
        try:
            self.processor.watermark_text_transparency(self.img_path,
                                                       f"{self.img_name}_watermarked.png",
                                                       text=self.text_entry.get(),
                                                       position=(int(self.xaxis_entry.get()), int(self.yaxis_entry.get())),
                                                       size=int(self.size.get()),
                                                       color=self.color.get(),
                                                       opacity=int(self.transparency.get()))
        except AttributeError:
            messagebox.showinfo(title="Error", message="Please select an image to add watermark.")
        else:
            self.input_image = PhotoImage(file=f"{self.img_name}_watermarked.png")
            self.target_image = Label(self.window, image=self.input_image)
            self.target_image.place(x=50, y=10)

    def process_photo_watermark(self):
        watermark_size = int(self.wmsize.get().strip("%")) / 1000
        self.processor.transparent_watermark_background("spacesuit.png", "watermark.png", size=watermark_size)
        try:
            self.processor.watermark_photo_transparency(self.img_path,
                                                        f"{self.img_name}_watermarked.png",
                                                        "watermark.png",
                                                        position=(int(self.xaxis_entry.get()), int(self.yaxis_entry.get())))
        except AttributeError:
            messagebox.showinfo(title="Error", message="Please select an image to add watermark.")
        else:
            self.input_image = PhotoImage(file=f"{self.img_name}_watermarked.png")
            self.target_image = Label(self.window, image=self.input_image)
            self.target_image.place(x=50, y=10)





