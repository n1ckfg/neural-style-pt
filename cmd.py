from pathlib import Path


input_dir = "input"
output_dir = "output"
init = "image"


def format_command(content_image, style_image, cw, sw, tvw, ss, image_size, preserve_colors, num_iters, save_progress):
    
    ci = Path(input_dir, content_image)
    si = [Path(input_dir, s) for s in style_image.split(",")]
    stems = [p.stem for p in ([ci] + si)]
    prefix = "_".join(stems)
    suffix = "_sw{}_tvw{}_ss{}_ni{}".format(sw, tvw, ss, num_iters)
    oi = Path(output_dir, "{}{}.jpg".format(prefix, suffix))
    si = ",".join(str(img) for img in si)
    
    save_iter = "100" if save_progress else "0"
    original_colors = "1" if preserve_colors else "0"
    
    cmd = "neural_style.py -backend cudnn -cudnn_autotune -init {} -num_iterations {} -image_size {} -style_scale {} -content_weight {} -style_weight {} -tv_weight {} -style_image {} -content_image {} -original_colors {} -save_iter {} -output_image {}".format(init, num_iterations, image_size, style_scale, cw, sw, tvw, si, ci, original_colors, save_iter, oi)
    return cmd


if __name__ == "__main__":
    content_image = "content.jpg"
    style_image = "style1.jpg,style2.jpg"
    content_weight = 1
    style_scale = 0.5
    style_weight = 800
    tv_weight = 0
    image_size = 1000
    preserve_content_colors = False
    num_iterations = 2000
    save_progress = True
    print(format_command(content_image, style_image, content_weight, style_weight, tv_weight, style_scale, image_size, preserve_content_colors, num_iterations, save_progress))