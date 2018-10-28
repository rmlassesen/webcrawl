css = '''
        .pyRes {
            color: #FFFFFF;
            font-weight: bold;
            background-color: #0000AA;
            margin: 1px;
            padding: 5px;
            padding-left: 15px;
        }
        .wrapper {
            width: 70%;
            margin: auto;
        }
        .imgdiv {
            text-align: center;
        }
'''

def parse_string(string):
    div = '<div class="pyRes">' + string + '</div>'
    return div


def img_tag(img_name, img_path):
    tag = '<img src="' + img_path + '" alt="' + img_name + '" />'
    return tag


class Plot_Handler:
    def __init__(self):
        self.images = []
        self.imagetags = {}
        self.div = '<div class="imgdiv">'


    def new_plot(self, plot):
        new_plot = 'Plot' + str(len(self.images) + 1)
        plot_path = 'static/' + new_plot + '.png'
        self.images.append(new_plot)
        plot.savefig(plot_path)

        self.imagetags[new_plot] = self.div + img_tag(new_plot,plot_path) + '</div>'
        return self.imagetags[new_plot]




