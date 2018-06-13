# making a tag text file with python and jason in selected dir for asset browser
import os
import json
import os.path
tagFilesDir = r'L:\NXTPXLENT\pipe___RND\library\library_JSON_tags'
import maya.cmds as cmds
def newTagName(*args):
    tagNameTextField = cmds.textField('tagName', query=True, text=True)
    if tagNameTextField == '':
        tagNameTextField = s.lower()
        cmds.confirmDialog(title="ERROR...", message="Please enter a tag Name")
    else:
        # query the tag parent type for eg assets, shaders lightrigs or turntables
        tagFileTitle = []
        AssetsTagType = cmds.optionMenu('typeOfTag', query=True, value=True)
        if AssetsTagType == "Asset's":
            del tagFileTitle [:]
            tagFileTitle.append('assetsTag_')
        if AssetsTagType == "Shader's":
            del tagFileTitle [:]
            tagFileTitle.append('shadersTag_')
        if AssetsTagType == "Light Rig's":
            del tagFileTitle [:]
            tagFileTitle.append('lightRigsTag_')
        if AssetsTagType == "Turn Table Setup":
            del tagFileTitle [:]
            tagFileTitle.append('turnTablesTag_')

        # checking the dir if the tag name already exists
        tagName = tagNameTextField
        tagFileName = tagFileTitle[0] + tagName + '.txt'
        tagFile = os.path.join (tagFilesDir, tagFileName)

        tagFileChk = os.path.exists(tagFile)
        if tagFileChk == True:
            cmds.confirmDialog(title="ERROR...", message='Tag with this name already exists')
            cmds.textField("tagName", edit=True, tx='')
        else:
            tagFile = os.path.join (tagFilesDir, tagFileName)
            #writing json file
            with open(tagFile, 'w') as file:
                json.dump(
                {
                 'list': []
                 },file, sort_keys=True, indent=4)
            cmds.confirmDialog(title="Tag created successfully", message = 'Done')
            cmds.textField("tagName", edit=True, tx='')
            return tagFile

def tagUI(*args):
    tagUI = 'tagUi'
    if cmds.window(tagUI, exists=True):
    	cmds.deleteUI(tagUI)
    window = cmds.window('tagUi', title = 'New tag window', w=300)
    cmds.rowColumnLayout( numberOfColumns=1, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )
    tagCatg = cmds.optionMenu('typeOfTag', w=300, bgc=(.33, .33, .33))
    cmds.menuItem(label="Asset's")
    cmds.menuItem(label= "Shader's")
    cmds.menuItem(label="Light Rig's")
    cmds.menuItem(label="Turn Table Setup")
    cmds.text( label='New Tag Name' )
    nameOfNewTag = cmds.textField( 'tagName',  enterCommand=newTagName, w=300, h = 30 )
    createTagBtn = cmds.button('CreateTag', label="Create Tag", c=newTagName, h=40, w=300, bgc=(.55, .88, .99))
    cmds.showWindow( window )

tagUI()
