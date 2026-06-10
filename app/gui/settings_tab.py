import customtkinter as ctk

from app.database.postgres import (
db_manager
)

from app.scheduler.scheduler import (
AuraScheduler
)

class SettingsTab(ctk.CTkFrame):

```
def __init__(self, parent):

    super().__init__(parent)

    self.scheduler = (
        AuraScheduler()
    )

    self.build_ui()

def build_ui(self):

    title = ctk.CTkLabel(
        self,
        text="Settings",
        font=("Segoe UI", 26, "bold")
    )

    title.pack(
        anchor="w",
        padx=20,
        pady=20
    )

    settings_frame = ctk.CTkFrame(
        self
    )

    settings_frame.pack(
        fill="x",
        padx=20,
        pady=10
    )

    db_status = (
        "Connected"
        if db_manager.health_check()
        else "Disconnected"
    )

    db_label = ctk.CTkLabel(
        settings_frame,
        text=f"Database Status: {db_status}"
    )

    db_label.pack(
        anchor="w",
        padx=20,
        pady=(20, 10)
    )

    export_label = ctk.CTkLabel(
        settings_frame,
        text="Export Directory: exports/"
    )

    export_label.pack(
        anchor="w",
        padx=20,
        pady=10
    )

    theme_label = ctk.CTkLabel(
        settings_frame,
        text="Theme: Dark"
    )

    theme_label.pack(
        anchor="w",
        padx=20,
        pady=(10, 20)
    )

    scheduler_title = ctk.CTkLabel(
        self,
        text="Scheduler",
        font=("Segoe UI", 22, "bold")
    )

    scheduler_title.pack(
        anchor="w",
        padx=20,
        pady=(20, 10)
    )

    scheduler_frame = ctk.CTkFrame(
        self
    )

    scheduler_frame.pack(
        fill="x",
        padx=20,
        pady=10
    )

    self.schedule_url = (
        ctk.CTkEntry(
            scheduler_frame,
            width=500,
            placeholder_text=(
                "Target URL"
            )
        )
    )

    self.schedule_url.pack(
        padx=20,
        pady=(20, 10),
        anchor="w"
    )

    self.interval_entry = (
        ctk.CTkEntry(
            scheduler_frame,
            width=200,
            placeholder_text=(
                "Interval (Minutes)"
            )
        )
    )

    self.interval_entry.pack(
        padx=20,
        pady=10,
        anchor="w"
    )

    self.start_scheduler_button = (
        ctk.CTkButton(
            scheduler_frame,
            text="Start Scheduler",
            command=self.start_scheduler
        )
    )

    self.start_scheduler_button.pack(
        padx=20,
        pady=10,
        anchor="w"
    )

    self.stop_scheduler_button = (
        ctk.CTkButton(
            scheduler_frame,
            text="Stop Scheduler",
            command=self.stop_scheduler
        )
    )

    self.stop_scheduler_button.pack(
        padx=20,
        pady=(10, 20),
        anchor="w"
    )

    self.scheduler_status = (
        ctk.CTkLabel(
            scheduler_frame,
            text="Scheduler Status: Stopped"
        )
    )

    self.scheduler_status.pack(
        padx=20,
        pady=(0, 20),
        anchor="w"
    )

def start_scheduler(self):

    try:

        url = (
            self.schedule_url
            .get()
            .strip()
        )

        minutes = int(
            self.interval_entry
            .get()
            .strip()
        )

        if not url:

            self.scheduler_status.configure(
                text=(
                    "Scheduler Status: "
                    "URL Required"
                )
            )

            return

        self.scheduler.schedule_requests(
            url,
            minutes
        )

        self.scheduler.start()

        self.scheduler_status.configure(
            text=(
                f"Scheduler Running "
                f"({minutes} min)"
            )
        )

    except Exception as error:

        self.scheduler_status.configure(
            text=f"Error: {error}"
        )

def stop_scheduler(self):

    self.scheduler.stop()

    self.scheduler_status.configure(
        text="Scheduler Status: Stopped"
    )
```
