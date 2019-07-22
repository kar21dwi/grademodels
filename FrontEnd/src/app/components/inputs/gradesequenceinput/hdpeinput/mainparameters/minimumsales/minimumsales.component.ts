import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { CellValueChangedEvent, GridOptions } from 'ag-grid-community';

@Component({
	selector: 'app-minimumsales',
	templateUrl: './minimumsales.component.html',
	styleUrls: [ './minimumsales.component.css' ]
})
export class MinimumsalesComponent implements OnInit {
	public gridOptions: GridOptions;

	@Output() tablechange = new EventEmitter<any>();

	columnDefs = [];

	rowData = [];

	gradelist = [ 'F5400', 'P5300', 'P5200', 'P5200UV', 'B5500', 'B6401', 'HDT6', 'R5801', 'E5201S', 'E5201' ];
	arealist = [ 'Assam', 'Bihar', 'Himachal Pradesh', 'Goa' ];

	defaultColDef = {
		editable: this.checkEditFunction.bind(this),
		singleClickEdit: this.checkEditFunction.bind(this),
		resizable: true,
		width: 100
	};

	constructor() {
		this.columnDefs[0] = {
			headerName: 'Area Name',
			field: 'area',
			width: 200,
			editable: false,
			cellStyle: this.checkStyleFunction.bind(this)
		};
		for (let i = 1; i < 11; i++) {
			this.columnDefs[i] = { headerName: this.gradelist[i], field: this.gradelist[i - 1] };
		}

		for (let i = 0; i < 5; i++) {
			const obj: any = {};

			for (let k = 1; k < 11; k++) {
				if (i === 0) {
					obj[this.columnDefs[k].field] = k - 1;
				} else {
					const num = Math.floor(Math.random() * 100);

					obj[this.columnDefs[k].field] = num * 888;
				}
			}
			this.rowData[i] = obj;
			if (i === 0) {
				this.rowData[i].area = 'Grade Code';
			} else {
				this.rowData[i].area = this.arealist[i - 1];
			}
		}

		this.gridOptions = {
			rowData: this.rowData,
			columnDefs: this.columnDefs,
			defaultColDef: this.defaultColDef,
			suppressCellSelection: true,
			domLayout: 'autoHeight',

			onCellValueChanged: (event: CellValueChangedEvent) => {
				if (event.value !== String(event.oldValue)) {
					this.tablechange.emit(true);
				}
			}
		};
	}

	ngOnInit() {}

	checkEditFunction(params) {
		if (params.node.childIndex === 0) {
			return false;
		} else {
			return true;
		}
	}

	checkStyleFunction(params) {
		if (params.node.childIndex === 0) {
			return { fontFamily: 'Open Sans Regular' };
		} else {
			return { fontFamily: 'Open Sans Semibold' };
		}
	}
}
