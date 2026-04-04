import customtkinter as ctk
from datetime import datetime

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class CreativeSearchEngineUI:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Simple Search Engine")
        self.app.geometry("1180x760")
        self.app.minsize(1080, 700)
        self.app.configure(fg_color="#EEF3FB")

        # Hooks (to be connected by teammates)
        self.on_search = None
        self.on_load_files = None

        self.recent_queries = []
        self.subtitle_texts = [
            "Search across multiple text documents",
            "Fast keyword lookup with ranked results",
            "A simple engine with a polished interface"
        ]
        self.subtitle_index = 0

        self.build_ui()
        self.animate_subtitle()
        self.update_clock()

    def build_ui(self):
        self.outer = ctk.CTkFrame(self.app, fg_color="#EEF3FB", corner_radius=0)
        self.outer.pack(fill="both", expand=True, padx=24, pady=24)

        self.main_card = ctk.CTkFrame(
            self.outer,
            fg_color="#FFFFFF",
            corner_radius=28,
            border_width=1,
            border_color="#DCE3F0"
        )
        self.main_card.pack(fill="both", expand=True)
        self.main_card.grid_columnconfigure(0, weight=1)
        self.main_card.grid_columnconfigure(1, weight=3)
        self.main_card.grid_rowconfigure(0, weight=1)

        # LEFT PANEL
        self.left_panel = ctk.CTkFrame(
            self.main_card,
            fg_color="#4F46E5",
            corner_radius=24,
            width=290
        )
        self.left_panel.grid(row=0, column=0, sticky="nsew", padx=(18, 10), pady=18)
        self.left_panel.grid_propagate(False)

        ctk.CTkLabel(self.left_panel, text="🔎", font=("Arial", 42), text_color="white").pack(pady=(34, 10))
        ctk.CTkLabel(self.left_panel, text="Search Engine", font=("Arial", 28, "bold"), text_color="white").pack()
        ctk.CTkLabel(self.left_panel, text="Creative UI Demo", font=("Arial", 14), text_color="#DDE3FF").pack(pady=(6, 28))

        self.time_label = ctk.CTkLabel(self.left_panel, text="", font=("Arial", 15, "bold"), text_color="white")
        self.time_label.pack(pady=(0, 16))

        self.footer_note = ctk.CTkLabel(
            self.left_panel,
            text="UI Ready for Integration",
            font=("Arial", 13),
            text_color="#DDE3FF"
        )
        self.footer_note.pack(side="bottom", pady=28)

        # RIGHT PANEL
        self.right_panel = ctk.CTkFrame(self.main_card, fg_color="transparent")
        self.right_panel.grid(row=0, column=1, sticky="nsew", padx=(10, 18), pady=18)
        self.right_panel.grid_columnconfigure(0, weight=1)

        # Header
        header = ctk.CTkFrame(self.right_panel, fg_color="transparent")
        header.grid(row=0, column=0, sticky="ew", pady=(4, 14))

        ctk.CTkLabel(header, text="Simple Search Engine", font=("Arial", 30, "bold")).pack(anchor="w")

        self.animated_subtitle = ctk.CTkLabel(header, text="", font=("Arial", 15))
        self.animated_subtitle.pack(anchor="w", pady=(6, 0))

        # Controls
        controls = ctk.CTkFrame(self.right_panel, fg_color="#F8FAFF", corner_radius=22)
        controls.grid(row=1, column=0, sticky="ew", pady=(0, 18))

        # Load button
        self.load_button = ctk.CTkButton(
            controls,
            text="📂 Load Files",
            command=self.load_files_ui,
            height=45
        )
        self.load_button.pack(padx=20, pady=10, anchor="w")

        # Search
        search_frame = ctk.CTkFrame(controls, fg_color="transparent")
        search_frame.pack(fill="x", padx=20, pady=10)

        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Type a keyword...",
            height=45
        )
        self.search_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.search_entry.bind("<Return>", lambda e: self.search_ui())

        ctk.CTkButton(
            search_frame,
            text="Search",
            command=self.search_ui,
            width=120,
            height=45
        ).pack(side="right")

        # Results
        self.results_box = ctk.CTkScrollableFrame(self.right_panel)
        self.results_box.grid(row=2, column=0, sticky="nsew")
        self.right_panel.grid_rowconfigure(2, weight=1)

        self.show_message("UI ready. Connect backend.")

    # ------------------ UI LOGIC ONLY ------------------

    def load_files_ui(self):
        if self.on_load_files:
            self.on_load_files()

    def search_ui(self):
        query = self.search_entry.get().strip()

        if not query:
            self.show_message("Enter a keyword.")
            return

        if query not in self.recent_queries:
            self.recent_queries.append(query)

        if self.on_search:
            try:
                results = self.on_search(query)
                if results:
                    self.display_results(results)
                else:
                    self.show_message("No results returned.")
            except Exception:
                self.show_message("Error from backend.")
        else:
            self.show_message("Search backend not connected.")

    def display_results(self, results):
        self.clear_results()

        if not results:
            self.show_message("No results found.")
            return

        max_count = results[0][1] if results else 1

        for i, (filename, count) in enumerate(results, start=1):
            self.add_result_card(filename, count, i, max_count)

    def clear_results(self):
        for widget in self.results_box.winfo_children():
            widget.destroy()

    def show_message(self, text):
        self.clear_results()
        label = ctk.CTkLabel(self.results_box, text=text)
        label.pack(pady=20)

    def add_result_card(self, filename, count, rank_no, max_count):
        card = ctk.CTkFrame(self.results_box, corner_radius=15)
        card.pack(fill="x", padx=10, pady=8)

        ctk.CTkLabel(card, text=f"{filename}", font=("Arial", 15, "bold")).pack(anchor="w", padx=10, pady=(8, 0))
        ctk.CTkLabel(card, text=f"{count} matches").pack(anchor="w", padx=10)

        ctk.CTkLabel(card, text=f"#{rank_no}").pack(anchor="e", padx=10, pady=(0, 8))

    def animate_subtitle(self):
        self.animated_subtitle.configure(text=self.subtitle_texts[self.subtitle_index])
        self.subtitle_index = (self.subtitle_index + 1) % len(self.subtitle_texts)
        self.app.after(2000, self.animate_subtitle)

    def update_clock(self):
        self.time_label.configure(text=datetime.now().strftime("%I:%M:%S %p"))
        self.app.after(1000, self.update_clock)

    def run(self):
        self.app.mainloop()


# ------------------ RUN ------------------

if __name__ == "__main__":
    ui = CreativeSearchEngineUI()
    ui.run()