from pathlib import Path


input_dir = "input"
output_dir = "output"
init = "image"


def format_cmd(conf):
    args = {
        "-content_image": conf["content_image"],
        "-style_image": conf["style_image"],
        "-content_weight": conf["content_weight"],
        "-style_weight": conf["style_weight"],
        "-tv_weight": conf["tv_weight"],
        "-style_scale": conf["style_scale"],
        "-image_size": conf["image_size"],
        "-original_colors": 1 if conf["preserve_content_colors"] else 0,
        "-num_iterations": conf["num_iterations"],
        "-save_iter": 100 if conf["save_progress"] else 0,
        "-output_image": None,
        "-backend": "cudnn",
        "-cudnn_autotune": None,
        "-init": "image"
    }
    _set_image_paths(args)
    tokens = []
    for k in args:
        tokens.append(k)
        if args[k] is not None:
            tokens.append(str(args[k]))
    arg_str = " ".join(tokens)
    cmd = "neural_style.py {}".format(arg_str)
    return cmd


def _set_image_paths(args):
    ci = Path(input_dir, args["-content_image"])
    si = [Path(input_dir, s) for s in args["-style_image"].split(",")]
    stems = [p.stem for p in ([ci] + si)]
    prefix = "_".join(stems)
    sw = args["-style_weight"]
    tvw = args["-tv_weight"]
    ss = args["-style_scale"]
    ni = args["-num_iterations"]
    suffix = "_sw{}_tvw{}_ss{}_ni{}".format(sw, tvw, ss, ni)
    args["-content_image"] = str(ci)
    args["-style_image"] = ",".join(str(img) for img in si)
    args["-output_image"] = str(Path(output_dir, "{}{}.jpg".format(prefix, suffix)))


if __name__ == "__main__":
    config = {
        "content_image": "content.jpg",
        "style_image": "style1.jpg,style2.jpg",
        "content_weight": 1,
        "style_scale": 0.5,
        "style_weight": 800,
        "tv_weight": 0,
        "image_size": 1000,
        "preserve_content_colors": False,
        "num_iterations": 2000,
        "save_progress": True
    }
    print(format_cmd(config))