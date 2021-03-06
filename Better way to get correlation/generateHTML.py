#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
# vim:fileencoding=utf-8

import glob
import numpy as np

def getPlusSVG():
	tmp = '''
	<svg version="1.1" class="svgClass plusSVG" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;height: 30px;"  xml:space="preserve">
	<g>
		<g>
			<path d="M257,0C116.39,0,0,114.39,0,255s116.39,257,257,257s255-116.39,255-257S397.61,0,257,0z M392,285H287v107
				c0,16.54-13.47,30-30,30c-16.54,0-30-13.46-30-30V285H120c-16.54,0-30-13.46-30-30c0-16.54,13.46-30,30-30h107V120
				c0-16.54,13.46-30,30-30c16.53,0,30,13.46,30,30v105h105c16.53,0,30,13.46,30,30S408.53,285,392,285z"/>
		</g>
	</g>
	</svg>'''
	return tmp

def getMinusSVG():
	tmp = '''
	<svg version="1.1" class="svgClass minusSVG" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
		 viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;height: 30px;" xml:space="preserve">
	<g>
		<g>
			<path d="M257,0C116.39,0,0,114.39,0,255s116.39,257,257,257s255-116.39,255-257S397.61,0,257,0z M392,285H120
				c-16.54,0-30-13.46-30-30c0-16.54,13.46-30,30-30h272c16.53,0,30,13.46,30,30S408.53,285,392,285z" />
		</g>
	</g>
	</svg>'''
	return tmp

def write2HTML(contain):

	htmlFilePath = 'LG_vs_BPvar.html'
	htmlStarted = '''
	<!DOCTYPE html>
	<html>
	<head>
		<title>Correlation LG vs BP</title>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
		<style>
			body {
				padding-top: 50px;
			}
			.summaryTable, .summaryTable th, .summaryTable td {
				border: 1px solid black;
			}

			h1 {
				color: maroon;
				margin-left: 40px;
			}
			.nav{
				position: fixed;
				top: 0px;
				background: white;
				width: 100%;
			}
			.table th, td {
				text-align: center;
			}
			.tableTitle{
				font-weight: bold;
				font-size: 20px;
			}
			.bpNameLs span, .eventNameLs span{
				padding: 5px 10px;
			}
			.btn{
				padding:0px 0px;
				width: 100%;
				height: 100%;
				background: none;
			}
			.highlightCor{
			    background: pink;
    			text-decoration: underline;
			}
			.highlightPVal + .tooltip > .tooltip-inner {
				background-color: #f00;
				font-weight: bold;
				font-size: 15px;
			}
			.highlightPVal{
				border: red;
				border-style: dashed;
			}
			.plusSVG{
				display: none;
			}
			.corValue{
				background: #00cc99;
			    padding: 10px 15px;
			}
			.pValue{
				background: #ff9933;
			    padding: 10px 15px;
			}
			.oriData{
				height: 300px;
				overflow: auto;
			}
			.corValue b, strong {
				font-weight: 800;
				font-size: 20px;
			}
			.pValue b, strong {
				font-weight: 800;
				font-size: 20px;
			}
		</style>

		<script type="text/javascript">
			
$(function () {
  $('[data-toggle="tooltip"]').tooltip();
})

const EVENTNAMELS = 'eventNameLs';
const BPNAMELS = 'bpNameLs';
const BPCHECKBOX = 'bpCheckBox';
const EVENTCHECKBOX = 'eventCheckBox';
var collectArray = Array();
$( document ).ready(function() {

  function get_selected_checkboxes_array(className){
    var target = "." + className +" input.myoptions:checkbox[type=checkbox]:checked";
    collectArray = [];
    $(target).each(function(){collectArray.push($(this).val());}); 
    return collectArray
  }

  function setTheChange(){
    var targetBPClass;
    var targetEventClass;
    var tmpls;
    for(i = 0; i < bpnamels.length; i++) {
      targetBPClass = bpnamels[i];

      if (checked_bpname_ls.includes(targetBPClass) ) {
        
        for(j = 0; j < eventnamels.length; j++) {
          targetEventClass = eventnamels[j];
          if (checked_eventname_ls.includes(targetEventClass)){
            $('.corTable.' + targetBPClass + '.' + targetEventClass).css("display", "block");
          } else {
            $('.corTable.' + targetBPClass + '.' + targetEventClass).css("display", "none");
          }
        }
      } else {
        $('.corTable.' +targetBPClass).css('display', 'none');
      }
    }
  }


  
  

  function changeEvent(className, isBP){
    if (isBP){
      checked_bpname_ls = get_selected_checkboxes_array(className, isBP);
    } else {
      checked_eventname_ls = get_selected_checkboxes_array(className, isBP);
    }
    setTheChange();
  }


  function setMyOptionsByButton(class_name, checkedResult){
    $(class_name).click(function(){
      $(this).siblings('span').each(function(){
        $(this).children('input.myoptions').prop('checked', checkedResult);
      });
      var className = this.parentElement.classList;
      if(className.contains(EVENTNAMELS) ){
        changeEvent(EVENTNAMELS, false);
      } else if (className.contains(BPNAMELS) ){
        changeEvent(BPNAMELS, true);
      } else if (className.contains(BPCHECKBOX) ){
        applyTheChange(BPCHECKBOX, true);
      } else if (className.contains(EVENTCHECKBOX) ){
        applyTheChange(EVENTCHECKBOX, false);
      } 
    });
  }

  function get_selectedOriData_checkboxes_array(){
    var ch_list=Array();
    var bpcheckls = $(".bpCheckBox input:checkbox[type=checkbox]:checked")

    bpcheckls.each(function(){ch_list.push($(this).val());}); 
    $(".eventCheckBox input:checkbox[type=checkbox]:checked").each(function(){ch_list.push($(this).val());}); 
    return ch_list;
  }


  $('svg').height($('.tableTitle').height());

  $('.myData').css("display",'none');

  $('.minusSVG').css("display",'none');
  $('.plusSVG').css('display', 'inline-block');

  $('.collapseAll').click(function(){
    $('.myData').css("display",'none');
    $('.minusSVG').css("display",'none');
    $('.plusSVG').css('display', 'inline-block');
  });

  $('.expandAll').click(function(){
    $('.myData').css("display",'block');
    $('.plusSVG').css("display",'none');
    $('.minusSVG').css('display', 'inline-block');
  });

  $(".plusSVG").click(function() {
    var panel_body = $(this).parent().parent().parent().children().get(1);
    $(panel_body).css("display",'block');
    $(this).css("display",'none');
    var anotherSVG = $(this).siblings(0);
    $(anotherSVG).css('display','inline-block');
  });

  $(".minusSVG").click(function() {
    var panel_body = $(this).parent().parent().parent().children().get(1);
    $(panel_body).css("display",'none');
    $(this).css("display",'none');
    var anotherSVG = $(this).siblings().get(0);
    $(anotherSVG).css('display','inline-block');
  });

  $(".myoptions").each(function(){
    $(this).prop('checked', true);
  });


  const bpnamels = Array();
  $('div.bpNameLs > span > input').each(function(){ bpnamels.push($(this).val());	});
  const eventnamels = Array();
  $('div.eventNameLs > span > input').each(function(){ eventnamels.push($(this).val()); });
  var checked_bpname_ls;
  var checked_eventname_ls;
  checked_bpname_ls = get_selected_checkboxes_array(BPNAMELS, true);
  checked_eventname_ls = get_selected_checkboxes_array(EVENTNAMELS, false);
  
  var checked_rawBP_ls = get_selected_checkboxes_array(BPCHECKBOX, true);
  var checked_rawEventname_ls = get_selected_checkboxes_array(EVENTCHECKBOX, false);
  const rawBP_ls = Array();
  $('div.bpCheckBox > span > input').each(function(){ checked_rawBP_ls.push($(this).val());	});
  const rawEventname_ls = Array();
  $('div.eventCheckBox > span > input').each(function(){ checked_rawEventname_ls.push($(this).val());	});

function applyTheChange(className, isBP){
    if (isBP){
      checked_rawBP_ls = get_selected_checkboxes_array(className);
    } else {
      checked_rawEventname_ls = get_selected_checkboxes_array(className);
    }

    // const rawBP_ls = checked_rawBP_ls;
    // const rawEventname_ls = checked_rawEventname_ls;
    var targetBPClass;
    var targetEventClass;
    var tmpls;
    for(i = 0; i < rawBP_ls.length; i++) {
      targetBPClass = rawBP_ls[i];

      if (checked_rawBP_ls.includes(targetBPClass) ) {

        for(j = 0; j < rawEventname_ls.length; j++) {
          targetEventClass = rawEventname_ls[j];
          if (checked_rawEventname_ls.includes(targetEventClass)){
            $('.' + targetBPClass + '.' + targetEventClass).css("display", "block");
          } else {
            $('.' + targetBPClass + '.' + targetEventClass).css("display", "none");
          }
        }
      } else {
        tmpls = document.getElementsByClassName(targetBPClass);
        for (t = 0; t < tmpls.length; t ++){
          tmpls[t].style.display = 'none';
        }
      }
    }
  }

  var bPselectElement = document.querySelector('.bpCheckBox');
  bPselectElement.addEventListener('change', (event) => {
    console.log('he');
    applyTheChange(BPCHECKBOX, true)
  }); 

  var eventSelectElement = document.querySelector('.eventCheckBox');
  eventSelectElement.addEventListener('change', (event) => {
    applyTheChange(EVENTCHECKBOX, false)
  });

  var bpNameSelectElement = document.querySelector('.bpNameLs');
  bpNameSelectElement.addEventListener('change', (event) => {
    changeEvent(BPNAMELS, true);
  });

  var eventNameSelectElement = document.querySelector('.eventNameLs');
  eventNameSelectElement.addEventListener('change', (event) => {
    changeEvent(EVENTNAMELS, false);
  });



  setMyOptionsByButton('.not-myall-options', false);
  setMyOptionsByButton('.myall-options', true);
 
});



		</script>
	</head>
	<body>'''

	htmlEndingPart = '''
	</body>
	</html>'''

	contain = htmlStarted + contain + htmlEndingPart

	with open(htmlFilePath, 'w') as fw:
		fw.write(contain)

def getEventName(oneWord):
	return inv_eventNameDict.get(oneWord, oneWord)

def getTableName(oneWord, isClass):
	if 'ori_data' in oneWord:
		# tmp = oneWord.replace('.csv', '').split('_')
		name = nameDict.get(oneWord, oneWord) + ' for each bp'
	else:
		tmp = oneWord.replace('.csv', '').split('_')
		dataType =  tmp[1]#inv_eventNameDict.get(tmp[1],)
		bpType = tmp[-1]
		if isClass:
			name = 'class_{} class_{}'.format(dataType, bpType)
		else:
			name = '{} in <u>{}</u>'.format(getEventName(dataType), bpType)
	return name



def getCheckBoxHTML(ls, valueLs):
	# check box for bp type and events
	checkBox_tmpelate = '''<span class="form-check form-check-inline">
	<input class="form-check-input {}" type="checkbox" id="inlineCheckbox1" value="class_{}">
	<label class="form-check-label" for="inlineCheckbox1">{}</label>
	</span>'''

	for i in range(len(ls)):
		ls[i] = checkBox_tmpelate.format( 'myoptions', valueLs[i], ls[i])

	ls.append('''<button type="button" class="myall-options class_all"  >Check All</button>
				 <button type="button" class="not-myall-options class_notAll"  >Uncheck All</button>''')

	return ''.join(ls)

def generateOriDataTable(tableName, dataLs):
	dataLs = [i.strip() for i in dataLs]
	tableBody = '''
	<div class="panel panel-default">
		<div class="panel-heading">{}</div>
		<div class="panel-body oriData">
			<table class="table table-hover table-dark">
				<thead>
					<tr>
					  {}
					</tr>
				</thead>
				<tbody>
					{}
				</tbody>
			</table>

		</div>
	</div>'''

	# print(dataLs[0])
	thead_template = '''<th scope="col">{}</th>'''
	theadLs = dataLs[0].split(',')

	for i in range(len(theadLs)):
		theadLs[i] = thead_template.format(theadLs[i])

	theadLs = [thead_template.format("#")] + theadLs
	# print(theadLs)

	tbody_row_template = '''<tr class="{}">
	<th scope="row">{}</th>
	{}
	</tr>'''

	tbody_dataLs_template = '<td >{}</td>'

	dataLs = dataLs[1:]
	bpTypeLs = []
	eventTypeLs = []
	isNaN = lambda x : True if (x == 'NaN') else False

	dataLs = dataLs[0:]
	for i in range(len(dataLs)):
		rowdataLs1 = dataLs[i].split(',')
		
		bpName = rowdataLs1[0]
		if bpName not in bpTypeLs:
			bpTypeLs.append(bpName)

		rowdataLs1[0] = tbody_dataLs_template.format( bpName)
		eventName = getEventName(rowdataLs1[1])
		if eventName not in eventTypeLs:
			eventTypeLs.append(eventName)

		rowdataLs1[1] = tbody_dataLs_template.format( eventName) # Events Name
		rowdataLs1[2] = tbody_dataLs_template.format(rowdataLs1[2]) # Sub Number


		rowdataLs1[3] = tbody_dataLs_template.format('' if (isNaN(rowdataLs1[3])) else round(float(rowdataLs1[3]))) # normalBP
		rowdataLs1[4] = tbody_dataLs_template.format('' if (isNaN(rowdataLs1[4])) else round(float(rowdataLs1[4])))
		rowdataLs1[5] = tbody_dataLs_template.format('' if (isNaN(rowdataLs1[5])) else round(float(rowdataLs1[5]), 1))
		rowdataLs1[6] = tbody_dataLs_template.format('' if (isNaN(rowdataLs1[6])) else round(float(rowdataLs1[6])) )
		rowdataLs1[7] = tbody_dataLs_template.format('' if (isNaN(rowdataLs1[7])) else round(float(rowdataLs1[7]), 2)) # temporarl Location
		rowdataLs1[8] = tbody_dataLs_template.format('' if (isNaN(rowdataLs1[8])) else rowdataLs1[8]) # total events
		rowdataLs1[9] = tbody_dataLs_template.format('' if (isNaN(rowdataLs1[9])) else rowdataLs1[9]) # overlapping events
		rowdataLs1[10] = tbody_dataLs_template.format('' if (isNaN(rowdataLs1[10])) else round(float(rowdataLs1[10]), 2)) # equation slope
		rowdataLs1[11] = tbody_dataLs_template.format('' if (isNaN(rowdataLs1[11])) else round(float(rowdataLs1[11]), 2)) # regression slope

		dataLs[i] = ''.join(rowdataLs1)
		dataLs[i]  = tbody_row_template.format('class_{} class_{}'.format(bpName, eventName), i+1, ''.join(rowdataLs1))

	if len(eventTypeLs) > 1:
		bpCheckBoxHTML = getCheckBoxHTML(bpTypeLs, bpTypeLs)
	else:
		bpCheckBoxHTML = ''
	
	if len(eventTypeLs) > 1:
		eventCheckBoxHTML = getCheckBoxHTML(eventTypeLs, eventTypeLs)
	else:
		eventCheckBoxHTML = ''

	

	div_contain = '<div class=" tableTitle">{}</div><div class="bpCheckBox ori_data_checkbox">{}</div><div class="eventCheckBox ori_data_checkbox">{}</div>'.format(
							getTableName(tableName, 0), bpCheckBoxHTML, eventCheckBoxHTML)

	tableHTML = tableBody.format(div_contain, ''.join(theadLs), ''.join(dataLs))

	return tableHTML

def getLimitCount(tmpMatrix, isCorr):
	size = tmpMatrix.shape
	rolCount = size[0]
	colCount = size[1]

	result_rowLs = np.zeros(rolCount)
	for i in range(rolCount):
	    oneRow = tmpMatrix[i, :].reshape(colCount,1)
	    if isCorr:
	    	result_rowLs[i] = sum(1 if abs(x) >= cor_limit else 0 for x in oneRow)
	    else:
	    	result_rowLs[i] = sum(1 if x < pVal_limit else 0 for x in oneRow)
	# print(result_rowLs)

	result_colLs = np.zeros(colCount)
	for i in range(colCount):
	    oneCol = tmpMatrix[:, i]
	    if isCorr:
	    	result_colLs[i] = sum(1 if abs(x) >= cor_limit else 0 for x in oneCol)
	    else:
	    	result_colLs[i] = sum(1 if x < pVal_limit else 0 for x in oneCol)

	
	totalNum = int(sum(result_colLs))

	return [result_rowLs, result_colLs, totalNum]

def getPercentage(num, deno):
	return round(num*100/(deno), 1)

def generateCorTable(tableName, dataLs):
	dataLs = [i.strip() for i in dataLs]
	tableBody = '''
	<div class="panel panel-default corTable {}">
		<div class="panel-heading">{}</div>
		<div class="panel-body myData">
			<table class="table table-hover table-dark">
				<thead>
					<tr>
					  {}
					</tr>
				</thead>
				<tbody>
					{}
				</tbody>
			</table>
			{}
		</div>
	</div>'''

	className = getTableName(tableName, 1)
	print(className)

	# print(dataLs[0])
	thead_template = '''<th scope="col">{}</th>'''
	theadLs = dataLs[0].split(',')

	for i in range(len(theadLs)):
		theadLs[i] = thead_template.format(theadLs[i])

	theadLs = [thead_template.format("#")] + theadLs
	# print(theadLs)
	
	#--------------------------------------------------------------------------
	tbody_row_template = '''
	<tr>
		<th scope="row">{}</th>
		{}
	</tr>'''

	tbody_dataLs_templateWtToggle = '''
		<td>
			<button type="button" class="btn btn-secondary {} {}" data-toggle="tooltip" data-placement="top" title="p-value: {}">{}</button>
		</td>
	'''
	tbody_dataLs_templateWOToggle = '''
		<td>
			<button type="button" class="btn btn-secondary {} {}"  title="p-value: {}">{}</button>
		</td>
	'''

	tbody_dataLs_template = '<td>{}</td>'

	dataLs = dataLs[1:]

	eventTypeLs = []
	notNaN = lambda x : True if (x != 'NaN') else False

	# dataLs = dataLs[0:5]
	# for i in range(5):
	i = 0
	if len(dataLs)%2 != 0:
		print('Data ERROR: Correlation not follow with p value...')
		return

	dataLen = len(dataLs)//2
	columnNum = len(dataLs[0].split(','))-1

	corMatrix = np.zeros(dataLen*columnNum).reshape(dataLen, columnNum)
	pValMatrix = np.zeros(dataLen*columnNum).reshape(dataLen, columnNum)

	dataContainer = dataLen*[None] 
	rowNameLs = dataLen*[None] 
	# dataContainer[:] = None
	while i < dataLen:

		rowdataLs1 = dataLs[i*2].split(',')
		rowPvalLs1 = dataLs[i*2+1].split(',')
		
		corMatrix[i,:] = rowdataLs1[1:]
		pValMatrix[i,:] = rowPvalLs1[1:]

		# for adding row name
		rowName = rowdataLs1[0].replace('"','')
		rowNameLs[i] = rowName
		rowdataLs1[0] = tbody_dataLs_template.format('<b>' + rowName + '</b>')

		# for adding rest of cor val
		rIdx = 1
		while rIdx < len(rowdataLs1):
			corVal = float(rowdataLs1[rIdx])
			pVal = float(rowPvalLs1[rIdx])
			insert_pvalClass = ''
			insert_pval = pVal
			insert_corClass = ''
			insert_corVal = corVal

			if pVal < pVal_limit:
				insert_pvalClass = pVal_className
	
			if abs(corVal) >= cor_limit:
				insert_corClass = cor_className

			if insert_pvalClass != '': # only p val significant need toggle function
				rowdataLs1[rIdx] = tbody_dataLs_templateWtToggle.format(insert_corClass, insert_pvalClass, insert_pval, insert_corVal) 
			else:
				rowdataLs1[rIdx] = tbody_dataLs_templateWOToggle.format(insert_corClass, insert_pvalClass, insert_pval, insert_corVal) 
			rIdx += 1
		
		# print(rowdataLs1)
		dataContainer[i]  = tbody_row_template.format(i+1, ''.join(rowdataLs1))
		i +=1

	# get data for summary table
	[corRowLs, corColLs, corTotal] = getLimitCount(corMatrix, 1)
	[pValRowLs, pValColLs, pvalTotal] = getLimitCount(pValMatrix, 0)
	totCorSize = corMatrix.size
	# generate summary table
	summaryTable = '''
	<div>The quantity of correlation and p-value reach the threshold in {}</div>

	<table class="summaryTable table table-hover table-dark">
	<tr>
		{}
	</tr>
	<tr>
		{}  
	</tr>
	</table>'''

	summaryTableTd2 = '<th colspan="2">{}</th> '
	summaryTableTd = '<td class="corValue" style="background: #00cc99;">{}</td><td class="pValue" style="background: #ff9933;">{}</td>'
	headerNameLs = theadLs[2:]
	headerNameLs = [i.replace('scope="col"', 'colspan="2"') for i in headerNameLs]
	headerValLs = headerNameLs[:]
	for i in range(len(headerNameLs)):
		headerValLs[i] = summaryTableTd.format(int(corColLs[i]), int(pValColLs[i]))

	summaryTable4Col = summaryTable.format('Loop gain', ''.join(headerNameLs), ''.join(headerValLs))

	
	headerValLs = rowNameLs[:]
	for i in range(dataLen):
		rowNameLs[i] = summaryTableTd2.format(rowNameLs[i])
		headerValLs[i] = summaryTableTd.format(int(corRowLs[i]), int(pValRowLs[i]))		

	summaryTable4Row = summaryTable.format('Blood Pressure variables',''.join(rowNameLs), ''.join(headerValLs))

	summaryTable = summaryTable4Col + summaryTable4Row

	div_contain = '<div >{}{} <span class=" tableTitle">Data in {} | Num of Cor: {} ({} %)| Num of p-value: {} ({} %)</span></div>'.format( 
						getPlusSVG(), getMinusSVG(), getTableName(tableName, 0), 
									corTotal, getPercentage(corTotal,totCorSize), pvalTotal, getPercentage(pvalTotal,totCorSize))

	# tableHTML = tableBody.format(className,  div_contain, '', '', summaryTable)
	tableHTML = tableBody.format(className, div_contain, ''.join(theadLs), ''.join(dataContainer), summaryTable)

	return [tableHTML, corTotal, pvalTotal, totCorSize]


def sumTheSummary(mat):
    (row, col) = mat.shape
    # print(row, col)

    result = sum(mat[i,:] for i in range(row-1))
    mat[row-1,:] = result

    result = sum(mat[:,i] for i in range(col-1))
    mat[:,col-1] = result

    return mat

def getSummaryTd(mat, totMat,  htmlFormat):
	(row, col) = mat.shape
	result = [None] * row
	for r in range(row):
	    result[r] = [htmlFormat.format(int(mat[r,c]), getPercentage(int(mat[r,c]), int(totMat[r,c])) ) for c in range(col)]

	return result

def getSummaryTable(eventNameLs, oriBpNameLs, corMatrix, pValMatrix, totalMatrix):
	totalMatrix[totalMatrix == 0] = 1

	oriBpNameLs.append('Total')
	summarytableHTML = '''
	<div>
		<table class="table table-hover table-dark">
			{}
			{}
		</table>
	</div>
	'''
	summaryheader = [None] * (len(eventNameLs)+2)
	summaryTH = '''
			<th >
				{}
			</th>'''

	summaryTr = '''<tr>{}</tr>'''
	summaryheader[0] = summaryTH.format('#')

	summaryTH = '''
			<th colspan="2">
				{}
			</th>'''
	for c in range(len(eventNameLs)):
		summaryheader[c+1] = summaryTH.format(eventNameLs[c])
	summaryheader[-1] = summaryTH.format('Total')

	summaryCorLs = getSummaryTd(corMatrix, totalMatrix, '<td class="corValue">{} ({} %)</td>')
	summaryPValLs = getSummaryTd(pValMatrix, totalMatrix, '<td class="pValue">{} ({} %)</td>')
	# combine the cor td with p val td
	summaryLs = [None] * len(summaryCorLs)
	for i in range(len(summaryCorLs)):
		oneCorRow = summaryCorLs[i]
		summaryLs[i] = [ oneCorRow[o] + summaryPValLs[i][o] for o in range(len(oneCorRow))]


	summaryTd = '<td>{}</td>'
	summaryBodyContain = [None] * len(summaryLs)
	for i in range(len(summaryLs)):
		oneSummaryRow = summaryTd.format(oriBpNameLs[i] )+ ''.join(summaryLs[i])
		summaryBodyContain[i] = summaryTr.format(oneSummaryRow)

	return summarytableHTML.format(''.join(summaryheader), ''.join(summaryBodyContain))

#------------------------------------------ Function Above--------------------------------


htmlHeader = '''
<ul class="nav nav-pills">
	<li role="presentation" class="collapseAll"><a href="#">Collapse all result</a></li>
	<li role="presentation" class="expandAll"><a href="#">Expand all result</a></li>
	<li role="presentation" class="corValue">Number of <u><b>Corrlation</b></u> greater than <b>{}</b></li>
	<li role="presentation" class="pValue">Number of <u><b>p-Value less</b></u> than <b>{}</b></li>
</ul>
<h1>This is a summary of the quantity of correlation and p-value reach the threshold.</h1>
<div style=" font-size: 20px; margin-left: 40px;">Note: There are lots of correlation in the 
<span style="font-weight: bold;color: darkred;text-decoration: underline dotted darkred;">Central and Mixed</span> 
apnea, which should be ignored due to lack of data. Not more than 100 events in all subjects in either types of these two events.</div>
'''

htmlContain = ''

pVal_limit = 0.05
cor_limit = 0.5
htmlHeader = htmlHeader.format(cor_limit, pVal_limit)

cor_className = 'highlightCor'
pVal_className = 'highlightPVal'
pVal_NO_className = 'PVal'

oriBpNameLs = ['SysBP', 'DiaBP', 'Map', 'PP']
bpNameLs = oriBpNameLs[:]
bpClassNameLs = [ 'class_{}'.format(i) for i in bpNameLs]
eventNameDict = {
'All Evnets Combined': 'OCHM' ,
'All Events w/o Hypopnea': 'OCM' ,
'Obstructive': 'O' ,
'Central': 'C' ,
'Mixed': 'M' ,
'Hypopnea': 'H' }

inv_eventNameDict = {v: k for k, v in eventNameDict.items()}

eventNameLs = list(eventNameDict.keys())
eventValLs = [eventNameDict[i] for i in eventNameLs]

summaryRowLen = len(bpNameLs) + 1
summaryColLen = len(eventNameLs) + 1
totCorMatrix = np.zeros(summaryRowLen*summaryColLen).reshape(summaryRowLen,summaryColLen )
totPValMatrix = np.zeros(summaryRowLen*summaryColLen).reshape(summaryRowLen,summaryColLen )
totMatrix = np.zeros(summaryRowLen*summaryColLen).reshape(summaryRowLen,summaryColLen )

nameDict = {
	'ori_data_nan.csv': eventNameLs[0],
	'ori_data_OCHM.csv': eventNameLs[1],
	'ori_data_OCM.csv': eventNameLs[2],
	'ori_data_H.csv': eventNameLs[-1],
}

allSummaryHTML = "<div class='allSummary'>{}</div>"


####### Get control panel
htmlContain += '<div class="bpNameLs myCheckBox">{}</div>'.format(getCheckBoxHTML(bpNameLs, bpNameLs))
htmlContain += '<div class="eventNameLs myCheckBox">{}</div>'.format(getCheckBoxHTML(eventNameLs, eventValLs))

fileLs = list(glob.iglob('*.csv', recursive=False))

count = 0
for file_name in fileLs[:]:
	if 'ori_data_' not in file_name and 'nan_H' not in file_name:
		print('{} Working on {}'.format(count, file_name))
		count += 1
		with open(file_name, 'r') as f:
			data = f.readlines()

		[oneTable, oneCorTotal, onePvalTotal, oneTot] = generateCorTable(file_name, data)

		fileName = file_name.split('.')[0]
		tmpFName = fileName.split('_')
		colIdx = eventValLs.index(tmpFName[1])
		rolIdx = oriBpNameLs.index(tmpFName[-1])

		totCorMatrix[rolIdx, colIdx] = oneCorTotal
		totPValMatrix[rolIdx, colIdx] = onePvalTotal
		totMatrix[rolIdx, colIdx] = oneTot


		htmlContain += oneTable

		if count%4 == 0:
			print('add')
			htmlContain += '<hr style="border-top: 5px dashed #000;">'


totCorMatrix = sumTheSummary(totCorMatrix)
totPValMatrix = sumTheSummary(totPValMatrix)
totMatrix = sumTheSummary(totMatrix)


summarytableHTML = getSummaryTable(list(eventNameDict.keys()), oriBpNameLs, totCorMatrix, totPValMatrix, totMatrix)

# <hr style="border-top: 5px dashed #000;">
htmlContain += '<h1 style="text-align:center;">Raw Data</h1>'

fileLs = list(glob.iglob('ori_data_*.csv', recursive=False))

for file_name in fileLs[:]:
	# print('Working on {}'.format(file_name))
	with open(file_name, 'r') as f:
		data = f.readlines()

	oneTable = generateOriDataTable(file_name, data)


	htmlContain += oneTable



# write2HTML(htmlHeader + htmlContain)
write2HTML(htmlHeader + summarytableHTML + htmlContain)

print('done')

# count number of class included to get the correlation count and p-value count
# python numpy to create matrix and get the count? for each row and column as well as the overall count?


# good events may be less than num of events 
