from docutils import nodes
from docutils.parsers.rst import Directive


class CommentBox(Directive):
    def run(self):
        env = self.state.document.settings.env  # sphinx.environment.BuildEnvironment
        config = env.config  # sphinx.config.Config
        if config["html_comment_box_id"] != "none":
            new_content = """
                .. raw:: html

                    <!-- begin wwww.htmlcommentbox.com --> <div id="HCB_comment_box"><a href="http://www.htmlcommentbox.com">Comment Box</a> is loading comments...</div> <link rel="stylesheet" type="text/css" href="https://www.htmlcommentbox.com/static/skins/bootstrap/twitter-bootstrap.css?v=0" /> <script type="text/javascript" id="hcb"> /*<!--*/ if(!window.hcb_user){hcb_user={};} (function(){var s=document.createElement("script"), l=hcb_user.PAGE || (""+window.location).replace(/'/g,"%27"), h="https://www.htmlcommentbox.com";s.setAttribute("type","text/javascript");s.setAttribute("src", h+"/jread?page="+encodeURIComponent(l).replace("+","%2B")+"&mod=**IdPlaceholder**"+"&opts=16798&num=10&ts=1666393980195");if (typeof s!="undefined") document.getElementsByTagName("head")[0].appendChild(s);})(); /*-->*/ </script> <!-- end www.htmlcommentbox.com -->
            """.replace("**IdPlaceholder**", str(config["html_comment_box_id"]).replace("&mod=", ""))

            new_content = new_content.split("\n")

            for i in range(int(len(self.content))):
                self.content[i] = ""

            new_content.append('')
            for idx, line in enumerate(new_content):
                self.content.data.insert(idx, line)
                self.content.items.insert(idx, (None, idx))

        node = nodes.container()
        self.state.nested_parse(self.content, self.content_offset, node)
        return node.children


def setup(app):
    app.add_config_value('html_comment_box_id', "none", 'html')
    app.add_directive("sphinxcommentbox", CommentBox)

    return {
        'version': '1.0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }