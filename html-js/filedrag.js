/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

(function() {
    
    var fileManager1 = new FileReader;
    var fileManager2 = new FileReader;
    
    var _binStart = "";
    var _binEnd = "";

	// getElementById
	function $id(id) {
		return document.getElementById(id);
	} 


	// output information
	function Output(msg) {
		var m = $id("messages");
		m.innerHTML = msg + m.innerHTML;
	}
    
	function OutputHash(eId, msg) {
        $("#"+eId+" .hash").html(msg);
	}


	// file drag hover
	function FileDragHover(e) {
		e.stopPropagation();
		e.preventDefault();
		e.target.className = (e.type == "dragover" ? "hover" : "");
	}


	// file selection
	function FileSelectHandler1(e) {

		// cancel event and hover styling
		FileDragHover(e);

		// fetch FileList object
		var files = e.target.files || e.dataTransfer.files;

		// process all File objects
		for (var i = 0, f; f = files[i]; i++) {
                    var hash = new hashMe(f, function OutputHash(msg) {
                                $id("firstfilehash").innerHTML = msg;
                          });
                    //ParseFile(f, i);
		}

	}

	function FileSelectHandler2(e) {

		// cancel event and hover styling
		FileDragHover(e);

		// fetch FileList object
		var files = e.target.files || e.dataTransfer.files;

		// process all File objects
		for (var i = 0, f; f = files[i]; i++) {
                var hash = new hashMe(f, function OutputHash(msg) {
                                $id("secondfilehash").innerHTML = msg;
                          });
                //ParseFile(f, i);
		}

	}
        
	// output file information
	function ParseFile(file, id) {
                
		Output(
			"<p id='"+ id +"'>File information: <strong>" + file.name +
			"</strong> type: <strong>" + file.type +
			"</strong> size: <strong>" + file.size +
			"</strong> <span style='color:green;'>hash: <strong class='hash'>" +
			"</strong></span> " +
            "</p>"
		);

        
        // added to process the hash of the files:
        var hash = new hashMe(file, function OutputHash(msg) {
                                $("#"+ id +" .hash").html(msg);
                          });

	}


	// initialize
	function Init() {

		var fileselect1 = $id("fileselect1"),
                    fileselect2 = $id("fileselect2"),
                    firstfile = $id("firstfile"),
                    secondfile = $id("secondfile"),
			filedrag = $id("filedrag"),
			submitbutton = $id("submitbutton");

		// file select
		fileselect1.addEventListener("change", FileSelectHandler1, false);
                fileselect2.addEventListener("change", FileSelectHandler2, false);
                
                firstfile.addEventListener("change", firstSelectHandler, false);
                secondfile.addEventListener("change", secondSelectHandler, false);

		// is XHR2 available?
		var xhr = new XMLHttpRequest();
		if (xhr.upload) {

			// file drop
			filedrag.addEventListener("dragover", FileDragHover, false);
			filedrag.addEventListener("dragleave", FileDragHover, false);
			filedrag.addEventListener("drop", FileSelectHandler, false);
			filedrag.style.display = "block";

			// remove submit button
			submitbutton.style.display = "none";
		}

	}

	// call initialization file
	if (window.File && window.FileList && window.FileReader) {
		Init();
	}


})();