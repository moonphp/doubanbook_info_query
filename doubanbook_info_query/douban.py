#Boa:Frame:Frame1

import wx
import json
import wx.richtext
import urllib2

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1PANEL1, wxID_FRAME1RICHTEXTCTRL1, 
 wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(8)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(687, 125), size=wx.Size(600, 478),
              style=wx.DEFAULT_FRAME_STYLE, title=u'doubanBook')
        self.SetClientSize(wx.Size(584, 440))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(584, 440),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(32, 64), size=wx.Size(376, 40),
              style=0, value=u'')
        self.textCtrl1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Tahoma'))
        self.textCtrl1.SetToolTipString(u'')
        self.textCtrl1.SetInsertionPoint(0)
        self.textCtrl1.SetThemeEnabled(False)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'\u8c46\u74e3\u4e00\u4e0b', name='button1',
              parent=self.panel1, pos=wx.Point(440, 64), size=wx.Size(75, 40),
              style=0)
        self.button1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Tahoma'))
        self.button1.SetToolTipString(u'\u641c\u7d22')
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'douban.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self.panel1, pos=wx.Point(136, 8),
              size=wx.Size(200, 50), style=0)
        self.staticBitmap1.SetToolTipString(u'')

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'\u8bf7\u8f93\u5165\u4e66\u540d\u5173\u952e\u5b57\u67e5\u627e(\u5982\uff1a\u897f\u6e38\u8bb0)',
              name='staticText1', parent=self.panel1, pos=wx.Point(152, 112),
              size=wx.Size(188, 17), style=0)
        self.staticText1.SetBackgroundColour(wx.Colour(244, 244, 244))
        self.staticText1.SetForegroundColour(wx.Colour(255, 128, 128))
        self.staticText1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'\u5fae\u8f6f\u96c5\u9ed1'))
        self.staticText1.SetToolTipString(u'')

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL1,
              parent=self.panel1, pos=wx.Point(8, 160), size=wx.Size(552, 272),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl1.SetLabel(u'richText')
        self.richTextCtrl1.SetEditable(False)
        self.richTextCtrl1.SetHelpText(u'')

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2, label=u'',
              name='staticText2', parent=self.panel1, pos=wx.Point(32, 136),
              size=wx.Size(0, 14), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.richTextCtrl1.SetEditable(True)
        self.richTextCtrl1.SetValue("")
        self.richTextCtrl1.SetEditable(False)
        URL = "https://api.douban.com/v2/book/search?q="+self.textCtrl1.GetValue().encode("utf-8")+"&start=0&count=20"
        res=urllib2.urlopen(URL)
        result=res.read()
        json_result=json.loads(result)
        #print json_result
        
        book_num=json_result["count"]
        print "the books:"+str(book_num)
        self.staticText2.SetLabel(u'\u4e00\u5171\u627e\u5230\u4e66\u7c4d\uff1a'+str(book_num)+u'\u672c\u3002')
        for i in range(0,book_num):
            print "returned book id"+str(i)
            book_id=json_result["books"][i]["id"]
            book_title=json_result["books"][i]["title"]
            book_isbn=""
            book_isbn10=""
            book_isbn13=""
            try:
                book_isbn10=json_result["books"][i]["isbn10"]
            except:
                print "No isbn10"
            try:
                book_isbn10=json_result["books"][i]["isbn13"]
            except:
                print "No isbn13"

            if book_isbn10=="":
                book_isbn=book_isbn13
            elif book_isbn13=="":
                book_isbn=book_isbn10
            else:
                book_isbn=isbn10+","+isbn13
            
            
            length=len(json_result["books"][i]["author"])
            print "length of authors"+str(length)
            book_author=""
            if length==0:
                book_author=""
            else :
                for j in range(0,length):
                    if j==0:
                        book_author=json_result["books"][i]["author"][j]
                    else:
                        book_author=book_author+","+json_result["books"][i]["author"][j]
            book_price=json_result["books"][i]["price"]
            book_pages=json_result["books"][i]["pages"]
            book_publisher=json_result["books"][i]["publisher"]
            book_summary=json_result["books"][i]["summary"]
            book_imageaddr=json_result["books"][i]["image"]
            print '''Book's image address:'''+"\n"+str(book_imageaddr)
            book_info=u'\u4e66\u53f7\uff1a'+book_id+"\n"+\
            u'\u4e66\u540d\uff1a'+book_title+"\n"+\
            u'ISBN\uff1a'+book_isbn+"\n"+\
            u'\u4f5c\u8005\uff1a'+book_author+"\n"+\
            u'\u4ef7\u683c\uff1a'+book_price+"\n"+\
            u'\u9875\u6570\uff1a'+book_pages+"\n"+\
            u'\u51fa\u7248\u793e\uff1a'+book_publisher+"\n"+\
            u'\u8be6\u7ec6\u4ecb\u7ecd\uff1a'+book_summary+"\n"+\
            u'\u56fe\u7247\u5730\u5740\uff1a'+book_imageaddr+"\n"
            
            self.richTextCtrl1.SetEditable(True)
            value=self.richTextCtrl1.GetValue()
            if value=="":
                value=book_info
            else :
                value=value+"\n\n\n\n"+book_info
            self.richTextCtrl1.SetValue(value)
            self.richTextCtrl1.SetEditable(False)
        
        event.Skip()
