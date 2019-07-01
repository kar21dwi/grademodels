import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { GradesequenceinputComponent } from './components/inputs/gradesequenceinput/gradesequenceinput.component';
import { HdpeinputComponent } from './components/inputs/gradesequenceinput/hdpeinput/hdpeinput.component';
import { NcuparametersComponent } from './components/inputs/gradesequenceinput/hdpeinput/commonparameters/ncuparameters/ncuparameters.component';

const routes: Routes = [
	{ path: '', component: HomeComponent },
	{ path: 'gradesequence', component: GradesequenceinputComponent },
	{ path: 'hdpeinput', component: HdpeinputComponent },
	{ path: 'ncuparameters', component: NcuparametersComponent }
];

@NgModule({
	imports: [ RouterModule.forRoot(routes) ],
	exports: [ RouterModule ]
})
export class AppRoutingModule {}
