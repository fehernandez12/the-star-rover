$(document).ready(
	function(){
		"use strict";
		$("#basic-datatable").DataTable(
			{
				keys:!0,
				language:{
					"lengthMenu": "Mostrar _MENU_ registros por página",
					"info": "Página _PAGE_ de _PAGES_",
					paginate:{
						previous:"<i class='mdi mdi-chevron-left'>",
						next:"<i class='mdi mdi-chevron-right'>"
					}
				},
				drawCallback: function(){
					$(".dataTables_paginate > .pagination").addClass(
						"pagination-rounded")
				}
			}
		);
	}
);