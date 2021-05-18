from pathlib import Path


input_dir = "input"
output_dir = "output"
init = "image"


class Command(object):

    def __init__(self, config):
        self.content_image = config["content_image"]
        self.style_image = config["style_image"]
        self.cw = config["content_weight"]
        self.sw = config["style_weight"]
        self.tvw = config["tv_weight"]
        self.ss = config["style_scale"]
        self.image_size = config["image_size"]
        self.preserve_colors = config["preserve_content_colors"]
        self.num_iters = config["num_iterations"]
        self.save_progress = config["save_progress"]

    def __repr__(self):
        return self.to_string()

    def to_string(self):
        ci = Path(input_dir, self.content_image)
        si = [Path(input_dir, s) for s in self.style_image.split(",")]
        stems = [p.stem for p in ([ci] + si)]
        prefix = "_".join(stems)
        suffix = "_sw{}_tvw{}_ss{}_ni{}".format(self.sw, self.tvw, self.ss, self.num_iters)
        oi = Path(output_dir, "{}{}.jpg".format(prefix, suffix))
        si = ",".join(str(img) for img in si)
        save_iter = "100" if self.save_progress else "0"
        original_colors = "1" if self.preserve_colors else "0"
        cmd = "neural_style.py -backend cudnn -cudnn_autotune -init {} -num_iterations {} -image_size {} -style_scale {} -content_weight {} -style_weight {} -tv_weight {} -style_image {} -content_image {} -original_colors {} -save_iter {} -output_image {}".format(init, self.num_iters, self.image_size, self.ss, self.cw, self.sw, self.tvw, si, ci, original_colors, save_iter, oi)
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
    c = Command(locals())
    print(c)