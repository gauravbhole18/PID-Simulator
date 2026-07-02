import customtkinter as ctk


class PIDSimulatorApp:

    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("PID Controller Simulator")
        self.root.geometry("1200x800")
#Frames
        self.control_frame = ctk.CTkFrame(self.root)
        self.control_frame.pack(side="left", 
                                fill="y", 
                                padx=10, 
                                pady=10)

        self.graph_frame = ctk.CTkFrame(self.root)

        self.graph_frame.pack(
            side = "right",
            fill = "both",
            expand = True,
            padx = "10",
            pady = "10"
        )



        #sliders

        self.kp_slider , self.kp_value = self.create_slider(
            self.control_frame,
            "kp",
            0,
            20,
            2.0
        )


        self.ki_slider , self.ki_value = self.create_slider(
            self.control_frame,
            "ki",
            0,
            20,
            2.0
        )


        self.kd_slider , self.kd_value = self.create_slider(
            self.control_frame,
            "kd",
            0,
            20,
            2.0
        )
        # self.kp_label = ctk.CTkLabel(
        #     self.control_frame,
        #     text = "kp"
        # )
        # self.kp_label.pack(pady=(20,5))

        # self.kp_slider = ctk.CTkSlider(
        #     self.control_frame,
        #     from_=0,
        #     to = 20
        # )
        # self.kp_slider.set(2.0)
        # self.kp_slider.pack(fill = "x", padx = 10)



    def create_slider(self,
                      parent,
                      label_text,
                      from_,
                      to,
                      default):
            frame = ctk.CTkFrame( parent)
            frame.pack(fill = "x", padx = 10, pady = 8)

            #slider label

            label = ctk.CTkLabel(
                frame,
                text = label_text
            )
            label.pack(anchor = "w")

            #current value

            value_label = ctk.CTkLabel(
                frame,
                text = f"{default:.2f}"
            )
            value_label.pack(anchor = "e")
            def update_value(value):
                value_label.configure(text = f"{value:.2f}")
            slider = ctk.CTkSlider(
                    frame,
                    from_ = from_,
                    to = to,
                    command = update_value
                    )
            slider.set(default)
            slider.pack(fill = "x", pady = 5)
            return slider, value_label

    def run(self):
        self.root.mainloop()