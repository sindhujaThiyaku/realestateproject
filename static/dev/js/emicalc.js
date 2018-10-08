$(document).ready(function(){
    $("#loangetinfo").click(function(){
	    var p = parseFloat($("#loanAmount").val())
		var r = parseFloat($("#interestRate").val())
		var n= Math.round($("#loanduration").val())
		var duration = $('input:radio[name="tenure"]:checked').val()
		var loanFrom = $('#loanfrom').val()
		var loanYearFrom = parseInt(loanFrom.split('-')[0])
		var loanMonthFrom = parseInt(loanFrom.split('-')[1])
		data = {'principal':p,'interest':r,'duration':n,'startMonth':loanMonthFrom,'startYear':loanYearFrom,'durationType':duration}
	    resultdata = ajaxCall('get','/emi/emi_result/',data,false)
	    if(resultdata.status=="Success"){
	    	console.log("resultdata===========>",resultdata)
	    }
    });
});


function ajaxCall(type,url,data,async){
	var status;
	$.ajax({
		type:type,
		url:url,
		data:data,
		async:async,
	}).done(function(json_data){
			status = json_data;
	});
	return status;
}