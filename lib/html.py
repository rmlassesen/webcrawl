css = '''
        ol {
            overflow:hidden;
            overflow-y:scroll;
            overflow-x:scroll;
            max-width: 35%;
            height: 700px;
            float:right;
            color: #FFFFFF;
            font-weight: light;
            background-color: #0000AA;
            margin: 1px;
            padding-top: 15px;
        }

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
            float:left
        }
        .imgdiv img {
            width: 765px;
        }
'''

def parse_string(string):
    div = '<div class="pyRes">' + string + '</div>'
    return div


def img_tag(img_name, img_path):
    tag = '<img src="' + img_path + '" alt="' + img_name + '" />'
    return tag

def ordered_list(o_list):
    list_tag = '<ol>\n'
    for elm in o_list:
        list_tag += '\t<li>' + elm + '</li>\n'

    list_tag += '</ol>'
    return list_tag


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




