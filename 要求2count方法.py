nowpos=0
            for i in range(0,dep_text.count("switch")):
                #self.casenum[i]='0'
                self.switchpos[i]=dep_text.index('switch',nowpos)
                nowpos=self.switchpos[i]+1
                #if words =='case':
            print(self.switchpos)
            print("switchnums: ", dep_text.count("switch"))
            #print("casenums: ",self.casenum)