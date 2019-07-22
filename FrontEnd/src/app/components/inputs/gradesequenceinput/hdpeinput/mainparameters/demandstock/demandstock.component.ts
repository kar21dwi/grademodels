import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { GridOptions, AutoWidthCalculator, CellValueChangedEvent, CellEditingStoppedEvent } from 'ag-grid-community';
import { equal } from 'assert';
import {
	CellKeyPressEvent,
	CellKeyDownEvent,
	CellEditingStartedEvent,
	CellClickedEvent
} from 'ag-grid-community/dist/lib/events';

@Component({
	selector: 'app-demandstock',
	templateUrl: './demandstock.component.html',
	styleUrls: [ './demandstock.component.css' ]
})
export class DemandstockComponent implements OnInit {
	public gridOptions: GridOptions;

	@Output() tablechange = new EventEmitter<any>();

	demandstock = {
		worksheet: 'HD_Demand_Stock',
		attributes: [
			{
				slNo: '0.0',
				grades: 'F5400',
				demand: '6282.703213610586',
				openingInventory: '3400.0',
				closingInventory: '2597.29678638941'
			},
			{
				slNo: '1.0',
				grades: 'P5300',
				demand: '5518.096463022508',
				openingInventory: '200.0',
				closingInventory: '1681.903536977492'
			},
			{
				slNo: '2.0',
				grades: 'P5200',
				demand: '1960.0',
				openingInventory: '200.0',
				closingInventory: '540.0'
			},
			{
				slNo: '3.0',
				grades: 'P5200UV',
				demand: '0.0',
				openingInventory: '0.0',
				closingInventory: '0.0'
			},
			{
				slNo: '4.0',
				grades: 'B5500',
				demand: '2134.0',
				openingInventory: '500.0',
				closingInventory: '866.0'
			},
			{
				slNo: '5.0',
				grades: 'B6401',
				demand: '6631.285476349101',
				openingInventory: '800.0',
				closingInventory: '1768.7145236508986'
			},
			{
				slNo: '6.0',
				grades: 'HDT6',
				demand: '0.0',
				openingInventory: '0.0',
				closingInventory: '0.0'
			},
			{
				slNo: '7.0',
				grades: 'R5801',
				demand: '0.0',
				openingInventory: '0.0',
				closingInventory: '0.0'
			},
			{
				slNo: '8.0',
				grades: 'E5201S',
				demand: '1248.8648233486942',
				openingInventory: '200.0',
				closingInventory: '651.1351766513058'
			},
			{
				slNo: '9.0',
				grades: 'E5201',
				demand: '787.4660633484162',
				openingInventory: '400.0',
				closingInventory: '612.5339366515838'
			}
		]
	};

	columnDefs = [
		{ headerName: 'Grade Code', field: 'slNo' },
		{ headerName: 'Grade Name', field: 'grades' },
		{ headerName: 'Demand', field: 'demand' },
		{ headerName: 'Opening Inventory', field: 'openingInventory' },
		{ headerName: 'Closing Inventory', field: 'closingInventory' }
	];

	rowData = [];

	defaultColDef = {
		editable: true,
		singleClickEdit: true,
		resizable: true,
		width: 180
	};

	constructor() {
		for (let k = 0; k < 10; k++) {
			this.rowData[k] = this.demandstock.attributes[k];
		}
		this.gridOptions = {
			rowData: this.rowData,
			columnDefs: this.columnDefs,
			defaultColDef: this.defaultColDef,
			suppressCellSelection: true,
			domLayout: 'autoHeight',

			onCellClicked: (event: CellClickedEvent) => {
				event.event.target.addEventListener('keydown', (e: KeyboardEvent) => {
					if ((e.keyCode < 48 || e.keyCode > 57) && e.keyCode !== 8 && e.keyCode !== 190) {
						e.preventDefault();
					}
				});
			},

			onCellValueChanged: (event: CellValueChangedEvent) => {
				if (event.value !== String(event.oldValue)) {
					this.tablechange.emit(true);
				}
			}
		};
	}

	ngOnInit() {}
}
