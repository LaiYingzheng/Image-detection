class HsvFilter:

    def init(self, hMin = None, vMin = None, sMin= None,
                    hMax = None, vMax = None, sMax = None,
                    sSub = None, sAdd = None, vSub = None,vAdd = None):
        self.hMin = hMin
        self.vMin = vMin
        self.sMin = sMin
        self.hMax = hMax
        self.vMax = vMax
        self.sMax = sMax
        self.sAdd = sAdd
        self.sSub = sSub
        self.vAdd = vAdd
        self.vSub = vSub

