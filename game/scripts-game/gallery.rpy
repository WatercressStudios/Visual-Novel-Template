#
# Generate gallery screen based on parameters below
#

image black = Solid("#000")

transform gallery_thumbnail(zoomval):
    zoom zoomval

transform fade_inout(duration=0.5):
    on show:
        alpha 0
        linear duration alpha 1
    on hide:
        linear duration alpha 0

screen gallery_item():
    modal True

    default hide_ui = False

    fixed at fade_inout:
        add "black"
    fixed align(0.5,0.5) at fade_inout:
        add gallery_get_image()

    if hide_ui:
        key (config.keymap['dismiss'] + config.keymap['hide_windows'] + config.keymap['game_menu']) action ToggleScreenVariable('hide_ui')
    else:
        key (config.keymap['dismiss'] + config.keymap['game_menu']) action Hide("gallery_item")
        key config.keymap['hide_windows'] action ToggleScreenVariable('hide_ui')

        frame:
            background 'gui/gallery/gallery_title_bg.png'
            xysize (991, 200)
            align (0.5, 1.0)
            add Frame('gui/gallery/gallery_title_deco.png', 100):
                align (0.5, 0.45)
                xysize (800, 40)
            text gallery_get_title():
                xysize (700, 50)
                align (0.5, 0.35)
                size 26
            button:
                idle_background im.MatrixColor('gui/gallery/icon_close.png', gui.idle_tint_matrix)
                selected_background 'gui/gallery/icon_close.png'
                hover_background im.MatrixColor('gui/gallery/icon_close.png', gui.hover_tint_matrix)
                align (0.34, 0.73)
                xysize (40, 40)
                action Hide("gallery_item")
            if 'variants' in gallery_current_image:
                button:
                    if 'variants' in gallery_current_image:
                        idle_background im.MatrixColor('gui/gallery/icon_prev.png', gui.idle_tint_matrix)
                        selected_background 'gui/gallery/icon_prev.png'
                        hover_background im.MatrixColor('gui/gallery/icon_prev.png', gui.hover_tint_matrix)
                    else:
                        background im.MatrixColor('gui/gallery/icon_prev.png', gui.idle_tint_matrix)
                    align (0.44, 0.73)
                    xysize (40, 40)
                    action gallery_prev_variation
                text gallery_get_variation_label():
                    xysize (40, 40)
                    align (0.495, 0.73)
                    text_align 0.5
                    size 26
                button:
                    if 'variants' in gallery_current_image:
                        idle_background im.MatrixColor('gui/gallery/icon_next.png', gui.idle_tint_matrix)
                        selected_background 'gui/gallery/icon_next.png'
                        hover_background im.MatrixColor('gui/gallery/icon_next.png', gui.hover_tint_matrix)
                    else:
                        background im.MatrixColor('gui/gallery/icon_next.png', gui.idle_tint_matrix)
                    align (0.56, 0.73)
                    xysize (40, 40)
                    action gallery_next_variation
            button:
                idle_background im.MatrixColor('gui/gallery/icon_eye.png', gui.idle_tint_matrix)
                selected_background 'gui/gallery/icon_eye.png'
                hover_background im.MatrixColor('gui/gallery/icon_eye.png', gui.hover_tint_matrix)
                align (0.65, 0.73)
                xysize (64, 40)
                action ToggleScreenVariable('hide_ui')

init python:
    gallery_search_query = "search the gallery"

    gallery_current_image = None
    gallery_variation_index = 0
    def gallery_next_variation():
        global gallery_variation_index, gallery_current_image
        if 'variants' in gallery_current_image:
            count = len(gallery_current_image["variants"].keys())
            if count > 1:
                gallery_variation_index += 1
                if gallery_variation_index >= count:
                    gallery_variation_index = 0
                renpy.restart_interaction()
    
    def gallery_prev_variation():
        global gallery_variation_index, gallery_current_image
        if 'variants' in gallery_current_image:
            count = len(gallery_current_image["variants"].keys())
            if count > 1:
                gallery_variation_index -= 1
                if gallery_variation_index < 0:
                    gallery_variation_index = count - 1
                renpy.restart_interaction()

    def gallery_get_title():
        global gallery_variation_index, gallery_current_image
        title = ''
        if 'variants' in gallery_current_image:
            keys = sorted(gallery_current_image["variants"].keys())
            title = gallery_current_image['title'] + ", " + keys[gallery_variation_index]
        else:
            title = gallery_current_image['title']
        if 'artist' in gallery_current_image:
            return title + '  {alpha=0.5}by ' + gallery_current_image['artist'] + '{/alpha}'
        else:
            return title

    def gallery_get_variation_label():
        global gallery_variation_index, gallery_current_image
        if 'variants' in gallery_current_image:
            count = len(gallery_current_image["variants"].keys())
            return str(gallery_variation_index+1) + "/" + str(count)
        else:
            return "1/1"

    def gallery_get_image():
        global gallery_variation_index, gallery_current_image
        if 'variants' in gallery_current_image:
            keys = sorted(gallery_current_image["variants"].keys())
            img = renpy.get_registered_image(gallery_current_image["variants"][keys[gallery_variation_index]])
        else:
            img = renpy.get_registered_image(gallery_current_image["image"])
        if type(img) is LayeredImage:
            return img.name
        return img
    
    def gallery_get_thumbnail_zoom(imgname):
        img = None
        if imgname:
            if renpy.has_image(imgname):
                img = renpy.get_registered_image(imgname)
            else:
                print("WARNING: Gallery thumbnail not found: " + imgname)
                return 0.0
            size = (384.0, 216.0)
            if type(img) is LayeredImage:
                size = renpy.image_size(renpy.get_registered_image(img.layers[0].image.name))
            else:
                size = renpy.image_size(img)
            xratio = size[0] / 384.0
            yratio = size[1] / 216.0
            return 1.0 / max(xratio, yratio)
        return 0.0

screen gallery(type="root"):

    default gallery_search_query_value = VariableInputValue('gallery_search_query', default=False)

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Gallery")):
        vbox:
            # # Input for search
            # button:

            #     key_events True
            #     ypos 0
            #     ysize 100
            #     xalign 0

            #     action gallery_search_query_value.Toggle()

            #     has vbox

            #     text "Search the gallery:":
            #         color gui.accent_color
            #         text_align 0
            #         size 20
            #     input:
            #         style "page_label_text"
            #         value gallery_search_query_value
            #         ypos 10
            #         xalign 0
            #         length gui.save_note_length
            #         color "#fff"
            #         size 20
            #         text_align 0
            #         xsize 685
            vpgrid:
                xsize 1600
                cols 3
                mousewheel True
                draggable True
                scrollbars "vertical"
                side_xalign 0.5
                yinitial 0.0
                xspacing 50
                yspacing 40
                left_margin 100
                right_margin 100

                if type == "root":
                    for folder in gallery_folders:
                        button:
                            background "gui/gallery/idle_folder.png"
                            hover_background "gui/gallery/hover_folder.png"
                            xsize 400
                            ysize 216
                            text folder["title"]:
                                align (0.52, 0.57)
                                size 22
                                text_align 0.5
                            action Show("gallery", type=folder["type"])

                else:

                    button:
                        background "gui/gallery/idle_folder_back.png"
                        hover_background "gui/gallery/hover_folder_back.png"
                        xsize 400
                        ysize 216
                        padding (0, 0)
                        margin (0, 0)
                        text "Back":
                            align (0.49, 0.57)
                            size 22
                            text_align 0.5
                        action Show("gallery", type="root")

                    for entry in gallery_content[type]:
                        # If entry["title"] contains gallery_search_query or if gallery_search_query is empty
                        if gallery_search_query in entry["title"].lower() or gallery_search_query == "search the gallery":
                            fixed:
                                xsize 400
                                ysize 216
                                if gallery_search_query in entry["title"].lower() or gallery_search_query == "search the gallery":
                                    fixed:
                                        xsize 384
                                        ysize 216
                                        xalign 1.0
                                        frame:
                                            if entry["thumbnail"]:
                                                background renpy.get_registered_image(entry["thumbnail"]) at gallery_thumbnail(gallery_get_thumbnail_zoom(entry["thumbnail"]))
                                            else:
                                                background renpy.get_registered_image(entry["image"]) at gallery_thumbnail(gallery_get_thumbnail_zoom(entry["image"]))
                                            xsize 384
                                            ysize 216
                                            padding (0, 0)
                                            margin (0, 0)
                                button:
                                    background "gui/gallery/thumbnail2_idle_overlay.png"
                                    hover_background "gui/gallery/thumbnail2_selected_overlay.png"
                                    xsize 400
                                    ysize 216
                                    padding (0, 0)
                                    margin (0, 0)
                                    action [ SetVariable('gallery_current_image', entry), SetVariable('gallery_variation_index', 0), Show("gallery_item") ]
                                    if "variants" in entry:
                                        text str(len(entry["variants"])):
                                            xalign 0.98
                                            yalign 0.03
                                            size 22
                                if 'artist' in entry:
                                    label entry["title"] + '  {alpha=0.5}by ' + entry["artist"] + '{/alpha}':
                                        align (1.0, 0.99)
                                        text_size 22
                                        text_text_align 0.0
                                        text_color '#fff'
                                        xsize 384
                                        padding (5, 0)
                                else:
                                    label entry["title"]:
                                        align (1.0, 0.99)
                                        text_size 22
                                        text_text_align 0.0
                                        text_color '#fff'
                                        xsize 384
                                        padding (5, 0)