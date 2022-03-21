import PySimpleGUI as sg
from pathlib import Path
import os
import threading

# techniques
import parrot_executor
import eda_executor
import no_context_executor
import first_best_wup_executor
import second_best_wup_executor
import first_best_w2v_executor
import second_best_w2v_executor
import hyper_w2v_executor
import hypon_w2v_executor

SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'

sg.theme('DarkTeal12')


def configure_parrot(max_return_phrases: int, do_diverse: bool, adequacy_threshold: float, fluency_threshold: float,
                     parameters_list: list):
    """
    Helper function that sets the parameters of Parrot
    :param max_return_phrases: Parrot argument max_return_phrases
    :param do_diverse: Parrot argument do_diverse
    :param adequacy_threshold: Parrot argument adequacy_threshold
    :param fluency_threshold: Parrot argument fluency_threshold
    :param parameters_list: list of parameters passed to the algorithm executor
    :return:
    """

    sg.theme('DarkGreen1')

    layout_conf = [
        [sg.Text('max_return_phrases ='), sg.Input("15", key='-MAX_RETURN_PHRASES-')],
        [sg.Text('do_diverse =        '), sg.Input("True", key='-DO_DIVERSE-')],
        [sg.Text('adequacy_threshold ='), sg.Input("5", key='-ADEQUACY_THRESHOLD-')],  # I will divide by 10
        [sg.Text('fluency_threshold = '), sg.Input("5", key='-FLUENCY_THRESHOLD-')],
        [sg.Button('Ok')]
    ]
    window_conf = sg.Window('Parameters', layout_conf)

    while True:

        event, values = window_conf.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Ok':
            # current values are saved checking they are legal

            if (window_conf['-MAX_RETURN_PHRASES-'].get()).isdigit():
                if 0 <= int(window_conf['-MAX_RETURN_PHRASES-'].get()) <= 15:
                    max_return_phrases = int(window_conf['-MAX_RETURN_PHRASES-'].get())
                else:
                    popup_message('max_return_phrases must be in the range (0,15)')
            else:
                popup_message('max_return_phrases must be an integer')
            if (window_conf['-DO_DIVERSE-'].get()) == "True" or (
                    window_conf['-DO_DIVERSE-'].get()) == "False":
                do_diverse = bool(window_conf['-DO_DIVERSE-'].get())
            else:
                popup_message('do_diverse must be True or False')
            if (window_conf['-ADEQUACY_THRESHOLD-'].get()).isdigit():
                if 0 <= int(window_conf['-ADEQUACY_THRESHOLD-'].get()) <= 10:
                    if int(window_conf['-ADEQUACY_THRESHOLD-'].get()) == 0:
                        adequacy_threshold = 0
                    else:
                        adequacy_threshold = int(window_conf['-ADEQUACY_THRESHOLD-'].get()) / 10
                else:
                    popup_message('adequacy_threshold must be in the range (0,10)')
            else:
                popup_message('adequacy_threshold must be an integer')
            if (window_conf['-FLUENCY_THRESHOLD-'].get()).isdigit():
                if 0 <= int(window_conf['-FLUENCY_THRESHOLD-'].get()) <= 10:
                    if int(window_conf['-FLUENCY_THRESHOLD-'].get()) == 0:
                        fluency_threshold = 0
                    else:
                        fluency_threshold = int(window_conf['-FLUENCY_THRESHOLD-'].get()) / 10
                else:
                    popup_message('fluency_threshold must be in the range (0,10)')
            else:
                popup_message('fluency_threshold must be an integer')

            if max_return_phrases is not None and do_diverse is not None and \
                    adequacy_threshold is not None and fluency_threshold is not None:
                # if all values are legal, put it in the list and close the window

                parameters_list.append(max_return_phrases)
                parameters_list.append(do_diverse)
                parameters_list.append(adequacy_threshold)
                parameters_list.append(fluency_threshold)

                window_conf.close()


def configure_eda(alpha_sr: float, alpha_ri: float, alpha_rs: float, alpha_rd: float, num_aug: int,
                  parameters_list: list):
    """
    Helper function that sets the parameters of Eda
    :param alpha_sr: Eda argument max_return_phrases
    :param alpha_ri: Eda argument do_diverse
    :param alpha_rs: Eda argument adequacy_threshold
    :param alpha_rd: Eda argument fluency_threshold
    :param num_aug: Eda argument num_aug
    :param parameters_list: list of parameters passed to the algorithm executor
    :return:
    """

    sg.theme('DarkGreen1')

    layout_conf = [
        [sg.Text('alpha_sr = '), sg.Input("1", key='-ALPHA_SR-')],
        [sg.Text('alpha_ri = '), sg.Input("0", key='-ALPHA_RI-')],
        [sg.Text('alpha_rs = '), sg.Input("0", key='-ALPHA_RS-')],  # I will divide by 10 if diff from 0
        [sg.Text('alpha_rd = '), sg.Input("0", key='-ALPHA_RD-')],
        [sg.Text('num_aug  = '), sg.Input("9", key='-NUM_AUG-')],
        [sg.Button('Ok')]
    ]
    window_conf = sg.Window('Parameters', layout_conf)

    while True:

        event, values = window_conf.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Ok':
            # current values are saved checking they are legal

            if (window_conf['-ALPHA_SR-'].get()).isdigit():
                if 0 <= int(window_conf['-ALPHA_SR-'].get()) <= 10:
                    if int(window_conf['-ALPHA_SR-'].get()) == 0:
                        alpha_sr = int(window_conf['-ALPHA_SR-'].get())
                    else:
                        alpha_sr = int(window_conf['-ALPHA_SR-'].get()) / 10
                else:
                    popup_message('alpha_sr must be in the range (0,10)')
            else:
                popup_message('alpha_sr must be an integer')
            if (window_conf['-ALPHA_RI-'].get()).isdigit():
                if 0 <= int(window_conf['-ALPHA_RI-'].get()) <= 10:
                    if int(window_conf['-ALPHA_RI-'].get()) == 0:
                        alpha_ri = int(window_conf['-ALPHA_RI-'].get())
                    else:
                        alpha_ri = int(window_conf['-ALPHA_RI-'].get()) / 10
                else:
                    popup_message('alpha_ri must be in the range (0,10)')
            else:
                popup_message('alpha_ri must be an integer')
            if (window_conf['-ALPHA_RS-'].get()).isdigit():
                if 0 <= int(window_conf['-ALPHA_RS-'].get()) <= 10:
                    if int(window_conf['-ALPHA_RS-'].get()) == 0:
                        alpha_rs = int(window_conf['-ALPHA_RS-'].get())
                    else:
                        alpha_rs = int(window_conf['-ALPHA_RS-'].get()) / 10
                else:
                    popup_message('alpha_rs must be in the range (0,10)')
            else:
                popup_message('alpha_rs must be an integer')
            if (window_conf['-ALPHA_RD-'].get()).isdigit():
                if 0 <= int(window_conf['-ALPHA_RD-'].get()) <= 10:
                    if int(window_conf['-ALPHA_RD-'].get()) == 0:
                        alpha_rd = int(window_conf['-ALPHA_RD-'].get())
                    else:
                        alpha_rd = int(window_conf['-ALPHA_RD-'].get()) / 10
                else:
                    popup_message('alpha_rd must be in the range (0,10)')
            else:
                popup_message('alpha_rd must be an integer')
            if (window_conf['-NUM_AUG-'].get()).isdigit():
                if 0 <= int(window_conf['-NUM_AUG-'].get()) <= 10:
                    num_aug = int(window_conf['-NUM_AUG-'].get())
                else:
                    popup_message('num_aug must be in the range (0,10)')
            else:
                popup_message('num_aug must be an integer')

            if alpha_sr is not None and alpha_ri is not None and \
                    alpha_rs is not None and alpha_rd is not None and num_aug is not None:
                # if all values are legal, put it in the list and close the window

                parameters_list.append(alpha_sr)
                parameters_list.append(alpha_ri)
                parameters_list.append(alpha_rs)
                parameters_list.append(alpha_rd)
                parameters_list.append(num_aug)

                window_conf.close()


def configure_no_context(always_subst: bool, parameters_list: list):
    """
    Helper function that sets the parameters of no_context technique
    :param always_subst: no_context_executor_func argument
    :param parameters_list: list of parameters passed to the algorithm executor
    :return:
    """

    sg.theme('DarkGreen1')

    layout_conf = [
        [sg.Text('always_subst', enable_events=True, text_color='black', k='-ALWAYS_SUBST_TEXT-', size=(15, 2)),
         sg.Checkbox('', enable_events=True, key='-ALWAYS_SUBST_CHECK_BOX-')],
        [sg.Button('Ok')]
    ]
    window_conf = sg.Window('Parameters', layout_conf)

    while True:

        event, values = window_conf.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Ok':
            # current values are saved checking they are legal

            if values['-ALWAYS_SUBST_CHECK_BOX-'] is True:
                always_subst = True
            else:
                always_subst = False

            if always_subst is not None:
                # if all values are legal, put it in the list and close the window

                parameters_list.append(always_subst)

                window_conf.close()  # se uno di questi è None finestra non si chiude, lo devi cambiare e mettere None


def configure_best(syn_vs_synsets: bool, syn_vs_term: bool, n_max: int, parameters_list: list):
    """
    Helper function that sets the parameters of first_best_wup, second_best_wup, first_best_w2v, second_best_w2v,
    hyper_w2v, hypon_w2v techniques
    :param syn_vs_synsets: argument of the executor
    :param syn_vs_term: argument of the executor
    :param n_max: argument of the executor
    :param parameters_list: list of parameters passed to the algorithm executor
    :return:
    """

    sg.theme('DarkGreen1')

    layout_conf = [
        [sg.Text('syn_vs_synsets', enable_events=True, text_color='black', k='-SYN_VS_SYNSETS_TEXT-', size=(15, 2)),
         sg.Checkbox('', enable_events=True, key='-SYN_VS_SYNSETS_CHECK_BOX-'),
         sg.Text('syn_vs_term', enable_events=True, text_color='black', k='-SYN_VS_TERM_TEXT-', size=(15, 2)),
         sg.Checkbox('', enable_events=True, key='-SYN_VS_TERM_CHECK_BOX-')],
        [sg.Text('n_max = '), sg.Input("100", key='-N_MAX-', size=(30, 2))],
        [sg.Button('Ok')]
    ]
    window_conf = sg.Window('Parameters', layout_conf)

    while True:

        event, values = window_conf.read()

        if event == sg.WIN_CLOSED:
            break

        if event == '-SYN_VS_SYNSETS_CHECK_BOX-':
            window_conf['-SYN_VS_TERM_CHECK_BOX-'].update(False)

        if event == '-SYN_VS_TERM_CHECK_BOX-':
            window_conf['-SYN_VS_SYNSETS_CHECK_BOX-'].update(False)

        if event == 'Ok':
            # current values are saved checking they are legal

            if not values['-SYN_VS_SYNSETS_CHECK_BOX-'] and not values['-SYN_VS_TERM_CHECK_BOX-']:
                popup_message('You have to choose between syn_vs_synsets or syn_vs term')
            elif values['-SYN_VS_SYNSETS_CHECK_BOX-']:
                syn_vs_synsets = True
                syn_vs_term = False
            elif values['-SYN_VS_TERM_CHECK_BOX-']:
                syn_vs_synsets = False
                syn_vs_term = True
            if (window_conf['-N_MAX-'].get()).isdigit():
                if 0 <= int(window_conf['-N_MAX-'].get()) <= 100:
                    n_max = int(window_conf['-N_MAX-'].get())
                else:
                    popup_message('n_max must be in the range (0,100)')
            else:
                popup_message('n_max must be an integer')

            if syn_vs_synsets is not None and syn_vs_term is not None and n_max is not None:
                # if all values are legal, put it in the list and close the window

                parameters_list.append(syn_vs_synsets)
                parameters_list.append(syn_vs_term)
                parameters_list.append(n_max)

                window_conf.close()


def collapse(layout, key):
    """
    Helper function that creates a Column that can be later made hidden, thus appearing "collapsed"
    :param layout: The layout for the section
    :param key: Key used to make this section visible / invisible
    :return: A pinned column that can be placed directly into your layout
    :rtype: sg.pin
    """

    return sg.pin(sg.Column(layout, key=key))


def popup_message(text: str):
    """
    Helper function that shows a message in error case
    :param text: text displayed in the popup window
    :return:
    """

    sg.theme('DarkRed1')
    layout = [

        [sg.Text(text)]

    ]
    window = sg.Window("Warning", layout)
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
    window.close()


def popup_text(filename: str, text: str):
    """
    Helper function that shows the text contained in filename
    :param text: text of the file
    :param filename: name of the file
    """

    sg.theme('DarkTeal12')
    layout = [

        [sg.Multiline(text, size=(80, 25)), ],

    ]
    # font = font non funziona
    window = sg.Window(filename, layout, modal=True, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
    window.close()


def execute(conf, parameters_list, filename, window):
    """
    Helper function that runs the method selected
    :param conf: method selected
    :param parameters_list: list of configurable parameters for the algorithm
    :param filename: file on which we run the method
    :param window: old window that will be closed by the function popup_output
    """

    print(f"Running {conf} on {filename}")
    print("with these parameters " + str(parameters_list))

    # the algorithm will return a dictionary {input_line: list_of_output_lines}
    output_dict = {}

    # setting the right executor
    if conf == 'Parrot':
        executor_func = parrot_executor.parrot_executor_func
    elif conf == 'Eda':
        executor_func = eda_executor.eda_executor_func
    elif conf == 'No_Context':
        executor_func = no_context_executor.no_context_executor_func
    elif conf == 'First_Best_wup':
        executor_func = first_best_wup_executor.first_best_wup_executor_func
    elif conf == 'Second_Best_wup':
        executor_func = second_best_wup_executor.second_best_wup_executor_func
    elif conf == 'First_Best_w2v':
        executor_func = first_best_w2v_executor.first_best_w2v_executor_func
    elif conf == 'Second_Best_w2v':
        executor_func = second_best_w2v_executor.second_best_w2v_executor_func
    elif conf == 'Hyper_w2v':
        executor_func = hyper_w2v_executor.hyper_w2v_executor_func
    elif conf == 'Hypon_w2v':
        executor_func = hypon_w2v_executor.hypon_w2v_executor_func

    thread_id = threading.Thread(target=executor_func, args=(filename, parameters_list, output_dict), daemon=True)
    print("Avvio thread " + conf + "...")
    thread_id.start()
    thread_id.join()
    print(output_dict)

    past_conf = None
    if filename.endswith("_rerun.txt"):
        index1 = filename.rfind("/")
        index2 = filename.rfind("_rerun")
        past_conf = filename[index1 + 1:index2]
        if os.path.exists(filename):
            os.remove(filename)

    input_list = list(output_dict.keys())  # se ci sono due frasi in input uguali diventano una sola
    popup_output(output_dict, input_list, conf, past_conf, window)


def popup_output(dict: dict, input_list: list, conf: str, past_conf: str, old_window):
    """
    Function that displays the output phrases and allows to modify, save and rerun
    :param dict: dictionary {input_1: [output_1.1, output_1.2...], input_2...}
    :param input_list: list of the keys of the dictionary (if two input phrases are equal they are counted only once)
    :param conf: configuration just ran (we need it for the name of the saved file)
    :param past_conf: configurations ran before (we need it for the name of the saved file)
    :param old_window: precedent output window
    :return:
    """

    sg.theme('DarkTeal12')

    if old_window is not None:
        # if present, the precedent output window will be closed
        old_window.close()

    count_rows = 0

    # counting the rows that i need
    for i in input_list:
        count_rows = count_rows + 1
        for j in range(len(dict[i])):
            count_rows = count_rows + 1

    layout_in = [[]]

    count = 0
    for i in input_list:
        # creating layout_in which is the layout for the outputs
        section = [[]]
        layout_in += [[sg.Text(SYMBOL_DOWN, enable_events=True, k='OPEN_' + str(count), text_color='black'),
                       sg.Text(i, enable_events=True, text_color='black', k='INPUT_TEXT_' + str(count), size=(150, 1)),
                       sg.Checkbox('', enable_events=True, key='CHECKBOX_IN_' + str(count))]]
        section += [[sg.Input(dict[i][j], k='OUTPUT_TEXT_' + str(count) + "." + str(j), size=(150, 1)),
                     sg.Checkbox('', enable_events=True, key='CHECKBOX_OUT_' + str(count) + "." + str(j))] for j in
                    range(len(dict[i]))]
        layout_in += [[collapse(section, 'SEC_' + str(count))]]

        count = count + 1

    conf_def = [
        [
            '&ReConfigure',
            ['&Parrot', '&Eda', '&No_Context', '&First_Best_wup', '&Second_Best_wup',
             '&First_Best_w2v', '&Second_Best_w2v', '&Hyper_w2v', '&Hypon_w2v']
        ]
    ]

    #  layout for buttons and for outputs
    layout = [
        [sg.MenubarCustom(conf_def, key='-RECONF-')],
        [sg.Text("Selected Configuration:             ", key='-SELECTED CONFIGURATION-')],
        [sg.Button('ReRun'), sg.Button("Save"), sg.Button('Exit')],
        [sg.HSep()],
        [sg.Checkbox('Check all', enable_events=True, key='Check_All'),
         sg.Text("         "),
         sg.Checkbox('Uncheck all', enable_events=True, key='Uncheck_All')],
        [sg.Checkbox('Check all inputs', enable_events=True, key='Check_All_Inputs'),
         sg.Text("  "),
         sg.Checkbox('Uncheck all inputs', enable_events=True, key='Uncheck_All_Inputs')],
        [sg.Checkbox('Check all outputs', enable_events=True, key='Check_All_Outputs'),
         sg.Text(" "),
         sg.Checkbox('Uncheck all outputs', enable_events=True, key='Uncheck_All_Outputs')],
        [sg.Checkbox('Close all', enable_events=True, key='Close_All'),
         sg.Text("         "),
         sg.Checkbox('Open all', enable_events=True, key='Open_All')],
        [sg.HSep()],
        [sg.Column(layout_in, size=(1200, 500), scrollable=True, key='-COLUMN-')]
    ]

    window = sg.Window("Outputs", layout)
    opened = True
    reconf = None
    output_file_index = 0
    parameters_list = []

    while True:

        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Parrot' or event == 'Eda' or event == 'No_Context' or \
                event == 'First_Best_wup' or event == 'Second_Best_wup' or \
                event == 'First_Best_w2v' or event == 'Second_Best_w2v' or \
                event == 'Hyper_w2v' or event == 'Hypon_w2v':

            reconf = values['-RECONF-']
            print(reconf)
            window['-SELECTED CONFIGURATION-'].update("Selected Configuration: " + reconf)

            parameters_list.clear()

            if reconf == 'Parrot':
                max_return_phrases = None
                do_diverse = None
                adequacy_threshold = None
                fluency_threshold = None
                configure_parrot(max_return_phrases, do_diverse, adequacy_threshold, fluency_threshold, parameters_list)

            elif reconf == 'Eda':
                alpha_sr = None
                alpha_ri = None
                alpha_rs = None
                alpha_rd = None
                num_aug = None
                configure_eda(alpha_sr, alpha_ri, alpha_rs, alpha_rd, num_aug, parameters_list)

            elif reconf == 'No_Context':
                always_subst = None
                configure_no_context(always_subst, parameters_list)

            elif reconf == 'First_Best_wup' or reconf == 'Second_Best_wup' or \
                    reconf == 'First_Best_w2v' or reconf == 'Second_Best_w2v' or \
                    reconf == 'Hyper_w2v' or reconf == 'Hypon_w2v':
                syn_vs_synsets = None
                syn_vs_term = None
                n_max = None
                configure_best(syn_vs_synsets, syn_vs_term, n_max, parameters_list)

        if event == 'ReRun':

            if reconf is None:
                popup_message("You have to choose a configuration")

            if not parameters_list:
                popup_message("You have to choose parameters and click Ok")

            else:

                selected_count = 0

                for i in range(len(input_list)):
                    if values['CHECKBOX_IN_' + str(i)] is True:
                        selected_count = selected_count + 1
                    for j in range(len(dict[input_list[i]])):
                        if values['CHECKBOX_OUT_' + str(i) + '.' + str(j)] is True:
                            selected_count = selected_count + 1

                if selected_count == 0:
                    popup_message("You have to select some items")

                else:
                    # save a file just for rerun, the name of the file contains the name of past ran configurations
                    # and the file does not contains 'Input Phrase:'
                    if past_conf is not None:
                        output_file = open(conf + "_" + past_conf + "_rerun.txt", "w")
                    else:
                        output_file = open(conf + "_rerun.txt", "w")
                    for i in range(len(input_list)):
                        if values['CHECKBOX_IN_' + str(i)] is True:
                            i_line = window['INPUT_TEXT_' + str(i)].get()
                            # you don't want empty lines in rerun file
                            if len(i_line.strip()) != 0:
                                if "\n" in i_line:
                                    output_file.write(i_line)
                                else:
                                    output_file.write(i_line + "\n")
                        for j in range(len(dict[input_list[i]])):
                            if values['CHECKBOX_OUT_' + str(i) + '.' + str(j)] is True:
                                o_line = window['OUTPUT_TEXT_' + str(i) + '.' + str(j)].get()
                                # you don't want empty lines in rerun file
                                if len(o_line.strip()) != 0:
                                    if "\n" in o_line:
                                        output_file.write(o_line)
                                    else:
                                        output_file.write(o_line + "\n")

                    output_file.close()

                    files = [f for f in os.listdir('.') if f.endswith('_rerun.txt')]
                    if len(files) != 1:
                        raise ValueError('should be only one rerun file in the current directory')

                    filename = files[0]

                    # you run the chosen configuration on rerun file
                    execute(reconf, parameters_list, filename, window)

        if event == 'Save':

            selected_count = 0
            for i in range(len(input_list)):
                if values['CHECKBOX_IN_' + str(i)] is True:
                    selected_count = selected_count + 1
                for j in range(len(dict[input_list[i]])):
                    if values['CHECKBOX_OUT_' + str(i) + '.' + str(j)] is True:
                        selected_count = selected_count + 1
            if selected_count == 0:
                popup_message("You have to select some items")

            else:
                # save file with output, the name of the file contains the name of past ran configurations
                # and the file does contains 'Input Phrase:'
                output_file_index = output_file_index + 1
                if past_conf is not None:
                    output_file = open(conf + "_" + past_conf + "_output_file_" + str(output_file_index) + ".txt", "w")
                else:
                    output_file = open(conf + "_output_file_" + str(output_file_index) + ".txt", "w")
                for i in range(len(input_list)):
                    if values['CHECKBOX_IN_' + str(i)] is True:
                        i_line = window['INPUT_TEXT_' + str(i)].get()
                        # you want empty lines, it is a result
                        if "\n" in i_line:
                            output_file.write("Input Phrase: " + i_line)
                        else:
                            output_file.write("Input Phrase: " + i_line + "\n")
                    for j in range(len(dict[input_list[i]])):
                        if values['CHECKBOX_OUT_' + str(i) + '.' + str(j)] is True:
                            o_line = window['OUTPUT_TEXT_' + str(i) + '.' + str(j)].get()
                            # you want empty lines, it is a result
                            if len(o_line.strip()) == 0:
                                output_file.write("Empty line\n")
                            elif "\n" in o_line:
                                output_file.write(o_line)
                            else:
                                output_file.write(o_line + "\n")

        if event == 'Check_All':
            for i in range(len(input_list)):
                window['CHECKBOX_IN_' + str(i)].update(True)
                for j in range(len(dict[input_list[i]])):
                    window['CHECKBOX_OUT_' + str(i) + '.' + str(j)].update(True)
            window['Uncheck_All'].update(False)

        if event == 'Uncheck_All':
            for i in range(len(input_list)):
                window['CHECKBOX_IN_' + str(i)].update(False)
                for j in range(len(dict[input_list[i]])):
                    window['CHECKBOX_OUT_' + str(i) + '.' + str(j)].update(False)
            window['Check_All'].update(False)

        if event == 'Check_All_Inputs':
            for i in range(len(input_list)):
                window['CHECKBOX_IN_' + str(i)].update(True)
            window['Uncheck_All_Inputs'].update(False)
            window['Uncheck_All'].update(False)

        if event == 'Uncheck_All_Inputs':
            for i in range(len(input_list)):
                window['CHECKBOX_IN_' + str(i)].update(False)
            window['Check_All_Inputs'].update(False)
            window['Check_All'].update(False)

        if event == 'Check_All_Outputs':
            for i in range(len(input_list)):
                for j in range(len(dict[input_list[i]])):
                    window['CHECKBOX_OUT_' + str(i) + '.' + str(j)].update(True)
            window['Uncheck_All_Outputs'].update(False)
            window['Uncheck_All'].update(False)

        if event == 'Uncheck_All_Outputs':
            for i in range(len(input_list)):
                for j in range(len(dict[input_list[i]])):
                    window['CHECKBOX_OUT_' + str(i) + '.' + str(j)].update(False)
            window['Check_All_Outputs'].update(False)
            window['Check_All'].update(False)

        i = 0
        while i < len(input_list):
            if event == 'OPEN_' + str(i):
                opened = not opened
                window['OPEN_' + str(i)].update(SYMBOL_DOWN if opened else SYMBOL_UP)
                window['SEC_' + str(i)].update(visible=opened)
            i = i + 1

        if event == 'Close_All':
            for i in range(len(input_list)):
                opened = False
                window['OPEN_' + str(i)].update(SYMBOL_DOWN)
                window['SEC_' + str(i)].update(visible=False)
            window['Open_All'].update(False)

        if event == 'Open_All':
            for i in range(len(input_list)):
                opened = True
                window['OPEN_' + str(i)].update(SYMBOL_UP)
                window['SEC_' + str(i)].update(visible=True)
            window['Close_All'].update(False)

    window.close()


def paraphrase_gui():
    """
    Function that starts the gui and allows to load a file, open it, configure the technique, run the method
    :return:
    """

    sg.theme('DarkTeal12')

    conf_def = [
        [
            '&Configure',
            ['&Parrot', '&Eda', '&No_Context', '&First_Best_wup', '&Second_Best_wup',
             '&First_Best_w2v', '&Second_Best_w2v', '&Hyper_w2v', '&Hypon_w2v']
        ]
    ]

    layout = [
        [sg.MenubarCustom(conf_def, key='-CONF-')],  # inside the variable values['-CONF-'] you have the algorithm name
        [sg.Text("Selected Configuration:             ", key='-SELECTED CONFIGURATION-')],
        [sg.Text("Choose a file: "), sg.Input(key='-INPUT-'), sg.FileBrowse()],
        [sg.T("               "), sg.Button('Run'), sg.Button("Open"), sg.Button('Exit')]
    ]

    window = sg.Window('Text Paraphrase', layout)

    conf = None
    filename = None
    parameters_list = []

    while True:

        event, values = window.read()

        if values['-INPUT-']:
            filename = values['-INPUT-']

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Parrot' or event == 'Eda' or event == 'No_Context' or \
                event == 'First_Best_wup' or event == 'Second_Best_wup' or \
                event == 'First_Best_w2v' or event == 'Second_Best_w2v' or \
                event == 'Hyper_w2v' or event == 'Hypon_w2v':

            conf = values['-CONF-']
            window['-SELECTED CONFIGURATION-'].update("Selected Configuration: " + conf)

            parameters_list.clear()

            if conf == 'Parrot':
                max_return_phrases = None
                do_diverse = None
                adequacy_threshold = None
                fluency_threshold = None
                configure_parrot(max_return_phrases, do_diverse, adequacy_threshold, fluency_threshold, parameters_list)

            elif conf == 'Eda':
                alpha_sr = None
                alpha_ri = None
                alpha_rs = None
                alpha_rd = None
                num_aug = None
                configure_eda(alpha_sr, alpha_ri, alpha_rs, alpha_rd, num_aug, parameters_list)

            elif conf == 'No_Context':
                always_subst = None
                configure_no_context(always_subst, parameters_list)

            elif conf == 'First_Best_wup' or conf == 'Second_Best_wup' or \
                    conf == 'First_Best_w2v' or conf == 'Second_Best_w2v' or \
                    conf == 'Hyper_w2v' or conf == 'Hypon_w2v':
                syn_vs_synsets = None
                syn_vs_term = None
                n_max = None
                configure_best(syn_vs_synsets, syn_vs_term, n_max, parameters_list)

        if event == "Run":

            if conf is None:
                popup_message('You have to choose a configuration')
            if not parameters_list:
                popup_message("You have to choose parameters and click Ok")

            else:

                if filename is None:
                    popup_message("You have to choose a file")
                else:
                    # you run the chosen configuration on file
                    execute(conf, parameters_list, filename, None)

        if event == 'Open':

            if filename is None:
                popup_message("You have to choose a file")
            else:
                if Path(filename).is_file():
                    try:
                        with open(filename, "rt", encoding='utf-8') as f:
                            text = f.read()
                        popup_text(filename, text)
                    except Exception as e:
                        print("Error: ", e)

    window.close()


if __name__ == '__main__':
    paraphrase_gui()
