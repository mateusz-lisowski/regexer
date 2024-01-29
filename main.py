import customtkinter as ctk
from dataclasses import dataclass


@dataclass
class OptionCheckbox:
    value: str
    checkbox: ctk.CTkCheckBox = None


@dataclass
class ValueCheckbox:

    frame: ctk.CTkFrame
    value: str

    options_frame: ctk.CTkFrame = None
    options: list[OptionCheckbox] = None
    checkbox: ctk.CTkCheckBox = None

    letters_options_frame: ctk.CTkFrame = None
    letters_options: list[OptionCheckbox] = None
    letters_checkbox: ctk.CTkCheckBox = None

    def __post_init__(self):
        self.options_frame = ctk.CTkFrame(self.frame)
        self.letters_options_frame = ctk.CTkFrame(self.options_frame)

    def show_options(self):
        if self.checkbox.get() == 1:
            self.options_frame.pack(padx=16, pady=16)
        else:
            self.options_frame.pack_forget()

    def show_letters_options(self):
        if self.letters_checkbox.get() == 1:
            self.letters_options_frame.grid(row=5, column=0, padx=16, pady=16, sticky='nsw')
        else:
            self.letters_options_frame.grid_forget()


class RegexerGUI:

    def __init__(self):

        # Define variables
        self.checkboxes: list[ValueCheckbox] = []
        self.separator = ' '

        # Root
        self.app = ctk.CTk()
        self.app.title('REGEXER')

        # Setting up themes
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        # Default fonts
        self.title_font = ('Arial', 16)
        self.text_font = ('Arial', 14)

        # App title label
        self.description_label = ctk.CTkLabel(
            self.app,
            text='Regexer - your own regex generating assistant!',
            font=self.title_font
        )

        # User's entry frame
        self.user_entry_frame = ctk.CTkFrame(self.app)

        # User's text entry
        self.textbox = ctk.CTkEntry(self.user_entry_frame, width=400, placeholder_text='Your text', font=self.text_font)
        self.textbox.grid(row=0, column=0, padx=16, pady=16)

        # Separators choice option window
        self.separator_menu = ctk.CTkOptionMenu(
            self.user_entry_frame,
            values=['space( )', 'colon(:)', 'semicolon(;)', 'hyphen(-)', 'coma(,)', 'custom'],
            command=self.show_custom_option
        )
        self.separator_menu.grid(row=0, column=1, padx=16, pady=16)

        # Separator custom entry
        self.separator_menu_custom_entry = ctk.CTkEntry(
            self.user_entry_frame,
            width=150,
            placeholder_text='Provide separator',
            font=self.text_font
        )

        # Buttons frame
        self.button_frame = ctk.CTkFrame(self.app)
        self.button_frame.grid_columnconfigure(0, weight=1)

        # Generate hints button
        self.generate_hints_button = ctk.CTkButton(
            self.button_frame,
            text='GENERATE HINTS',
            command=self.generate_hints
        )
        self.generate_hints_button.grid(row=0, column=0, padx=4)

        # Reset hints button
        self.reset_hints_button = ctk.CTkButton(
            self.button_frame,
            text='RESET HINTS',
            command=self.reset_hints
        )
        self.reset_hints_button.grid(row=0, column=1, padx=4)

        # Generate regex button
        self.generate_regex_button = ctk.CTkButton(
            self.button_frame,
            text='GENERATE REGEX',
            command=self.generate_regex
        )
        self.generate_regex_button.grid(row=0, column=2, padx=4)

        # Bottom frame
        self.bottom_regex_options_frame = ctk.CTkFrame(self.app)

        # Additional options frame
        self.additional_options_frame = ctk.CTkFrame(self.bottom_regex_options_frame)
        self.additional_options_frame.grid_columnconfigure(0, weight=1)

        # Options label
        self.options_label = ctk.CTkLabel(
            self.additional_options_frame,
            text='Additional options',
            font=self.title_font)
        self.options_label.grid(row=0, column=0, columnspan=3, padx=16, pady=8)

        # Option 1
        self.match_whole_line_cb = ctk.CTkCheckBox(self.additional_options_frame, text='Match whole line')
        self.match_whole_line_cb.grid(row=1, column=0, padx=16, pady=16)

        # Option 2
        self.gen_only_patterns_cb = ctk.CTkCheckBox(self.additional_options_frame, text='Generate only patterns')
        self.gen_only_patterns_cb.grid(row=1, column=1, padx=16, pady=16)

        # Option 3
        self.match_spaces_cb = ctk.CTkCheckBox(self.additional_options_frame, text='Match spaces')
        self.match_spaces_cb.grid(row=1, column=2, padx=16, pady=16)

        # Bottom regex frame
        self.bottom_frame = ctk.CTkFrame(self.bottom_regex_options_frame)
        self.bottom_frame.grid_columnconfigure(0, weight=1)

        # Bottom regex label
        self.regex_label = ctk.CTkLabel(
            self.bottom_frame,
            text='Generated pattern',
            font=self.title_font
        )
        self.regex_label.grid(row=0, column=0, padx=8, pady=8)

        # Bottom regex entry
        self.regex_textbox = ctk.CTkEntry(
            self.bottom_frame,
            width=400,
            placeholder_text='Here will appear generated regex',
            font=self.text_font
        )
        self.regex_textbox.grid(row=1, column=0, padx=16, pady=16)

        # Main scroll frame
        self.main_scroll_frame = ctk.CTkScrollableFrame(
            self.app,
            orientation=ctk.HORIZONTAL,
            width=1000,
            height=400
        )

        # Packing all frames
        self.description_label.pack(padx=16, pady=16)
        self.user_entry_frame.pack(padx=16, pady=16)
        self.button_frame.pack(padx=16, pady=8)
        self.bottom_frame.grid(row=0, column=0, padx=16, pady=16)
        self.additional_options_frame.grid(row=0, column=1, padx=16, pady=16)
        self.bottom_regex_options_frame.pack(padx=16, pady=16, side=ctk.BOTTOM)

        # Showing app
        self.app.mainloop()

    def set_separator(self):

        if self.separator_menu.get() == 'colon(:)':
            self.separator = ':'
        elif self.separator_menu.get() == 'semicolon(;)':
            self.separator = ';'
        elif self.separator_menu.get() == 'hyphen(-)':
            self.separator = '-'
        elif self.separator_menu.get() == 'coma(,)':
            self.separator = ','
        elif self.separator_menu.get() == 'custom':
            self.separator = self.separator_menu_custom_entry.get()
        else:
            self.separator = ' '

    def show_custom_option(self, event):
        if event == 'custom':
            self.separator_menu_custom_entry.grid(row=0, column=2, padx=16, pady=16)
        else:
            self.separator_menu_custom_entry.grid_forget()
            self.separator_menu_custom_entry.delete(0, ctk.END)
            self.separator_menu_custom_entry.insert(0, '')

    def generate_hints(self):

        self.set_separator()
        text = self.textbox.get()

        current_text = ''

        for checkbox in self.checkboxes:
            if checkbox:
                current_text += checkbox.value

        if current_text == ''.join(text.split(self.separator)):
            return

        self.reset_hints()
        self.main_scroll_frame.pack(padx=16, pady=16)
        for word in text.split(self.separator):

            word_checkbox = ValueCheckbox(
                value=word,
                frame=ctk.CTkFrame(self.main_scroll_frame),
            )
            word_checkbox.options = RegexerGUI.generate_options(word_checkbox)
            word_checkbox.checkbox = ctk.CTkCheckBox(
                word_checkbox.frame,
                text=word_checkbox.value,
                command=word_checkbox.show_options
            )

            word_checkbox.letters_checkbox = ctk.CTkCheckBox(
                word_checkbox.options_frame,
                text='Match symbols',
                command=word_checkbox.show_letters_options
            )

            word_checkbox.letters_options = RegexerGUI.generate_letters_option(word_checkbox)

            word_checkbox.letters_checkbox.grid(row=4, column=0, padx=16, pady=16, sticky='nsw')
            word_checkbox.checkbox.pack(padx=16, pady=16)
            self.checkboxes.append(word_checkbox)

        for checkbox in self.checkboxes:
            checkbox.frame.pack(padx=8, pady=8, side=ctk.LEFT, anchor=ctk.N)

    def reset_hints(self):
        for checkbox in self.checkboxes:
            checkbox.frame.pack_forget()
        self.main_scroll_frame.pack_forget()
        self.checkboxes.clear()

    def generate_regex(self):

        regex = r''

        for checkbox in self.checkboxes:

            partial_regex = r''

            if checkbox.checkbox.get() == 1:

                if checkbox.letters_checkbox.get() == 1:

                    for letter_checkbox in checkbox.letters_options:
                        if letter_checkbox.checkbox.get() == 1:
                            partial_regex += letter_checkbox.value

                else:

                    if checkbox.value.isalpha():
                        for option in checkbox.options:

                            if option.value == 'ignore_case':
                                if option.checkbox.get() == 1:
                                    partial_regex += '[a-zA-Z]'
                                elif checkbox.value[0].isupper():
                                    partial_regex += '[A-Z]'
                                else:
                                    partial_regex += '[a-z]'

                            if option.value == 'occurrences':
                                if option.checkbox.get() == 1:
                                    partial_regex += '{' + str(len(checkbox.value)) + '}'
                                else:
                                    partial_regex += '+'

                    elif checkbox.value.isdigit():

                        partial_regex += '[0-9]'

                        for option in checkbox.options:

                            if option.value == 'occurrences':
                                if option.checkbox.get() == 1:
                                    partial_regex += '{' + str(len(checkbox.value)) + '}'
                                else:
                                    partial_regex += '+'

                    elif checkbox.value.isalnum():
                        for option in checkbox.options:

                            if option.value == 'ignore_case':
                                if option.checkbox.get() == 1:
                                    partial_regex += '[a-zA-Z0-9]'
                                elif checkbox.value[0].isupper():
                                    partial_regex += '[A-Z0-9]'
                                else:
                                    partial_regex += '[a-z0-9]'

                            if option.value == 'occurrences':
                                if option.checkbox.get() == 1:
                                    partial_regex += '{' + str(len(checkbox.value)) + '}'
                                else:
                                    partial_regex += '+'
            else:
                if not self.gen_only_patterns_cb.get() == 1:
                    partial_regex += checkbox.value

            if partial_regex:
                regex += partial_regex + self.separator

        regex = regex.removesuffix(self.separator)

        if self.match_spaces_cb.get() == 1:
            regex = list(regex)
            for i in range(len(regex)):
                if regex[i] == ' ':
                    regex[i] = r'\s'

            regex = r''.join(regex)

        if self.match_whole_line_cb.get() == 1:
            regex = '^' + regex + '$'

        self.regex_textbox.delete(0, ctk.END)
        self.regex_textbox.insert(0, regex)

    @staticmethod
    def generate_options(master: ValueCheckbox) -> list[OptionCheckbox]:

        options: list[OptionCheckbox] = []

        if master.value.isdigit():

            option = OptionCheckbox(value='occurrences')
            option.checkbox = ctk.CTkCheckBox(master.options_frame, text='Number of occurrences')
            option.checkbox.grid(row=0, column=0, padx=16, pady=16, sticky='nsw')
            options.append(option)

        elif master.value.isalpha():

            option1 = OptionCheckbox(value='ignore_case')
            option1.checkbox = ctk.CTkCheckBox(master.options_frame, text='Ignore case')
            option1.checkbox.grid(row=0, column=0, padx=16, pady=16, sticky='nsw')
            options.append(option1)

            option2 = OptionCheckbox(value='occurrences')
            option2.checkbox = ctk.CTkCheckBox(master.options_frame, text='Number of occurrences')
            option2.checkbox.grid(row=1, column=0, padx=16, pady=16, sticky='nsw')
            options.append(option2)

        elif master.value.isalnum():

            option1 = OptionCheckbox(value='ignore_case')
            option1.checkbox = ctk.CTkCheckBox(master.options_frame, text='Ignore case')
            option1.checkbox.grid(row=0, column=0, padx=16, pady=16, sticky='nsw')
            options.append(option1)

            option2 = OptionCheckbox(value='occurrences')
            option2.checkbox = ctk.CTkCheckBox(master.options_frame, text='Number of occurrences')
            option2.checkbox.grid(row=1, column=0, padx=16, pady=16, sticky='nsw')
            options.append(option2)

        return options

    @staticmethod
    def generate_letters_option(master: ValueCheckbox) -> list[OptionCheckbox]:

        options: list[OptionCheckbox] = []

        for index, letter in enumerate(master.value):
            option = OptionCheckbox(value=letter)
            option.checkbox = ctk.CTkCheckBox(master.letters_options_frame, text=letter)
            option.checkbox.grid(row=0, column=index, padx=8, pady=8, sticky='e')
            options.append(option)

        return options


def main():
    RegexerGUI()


if __name__ == '__main__':
    main()
