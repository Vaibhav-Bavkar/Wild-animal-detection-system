// // import { Component } from '@angular/core';
// // import { RouterOutlet } from '@angular/router';

// // @Component({
// //   selector: 'app-root',
// //   imports: [RouterOutlet],
// //   templateUrl: './app.component.html',
// //   styleUrl: './app.component.css'
// // })
// // export class AppComponent {
// //   title = 'my-angular-app';
// // }




// // import { Component } from '@angular/core';
// // import { FileUploadComponent } from './file-upload/file-upload.component'; // Import the FileUploadComponent

// // @Component({
// //   selector: 'app-root',
// //   standalone: true, // Ensure this is a standalone component
// //   imports: [FileUploadComponent], // Add the FileUploadComponent here
// //   templateUrl: './app.component.html',
// // })
// // export class AppComponent {}



// // import { Component } from '@angular/core';
// // import { RouterOutlet } from '@angular/router'; // Import RouterOutlet
// // import { FileUploadComponent } from './file-upload/file-upload.component'; // Import other required components

// // @Component({
// //   selector: 'app-root',
// //   standalone: true, // Ensure it's a standalone component
// //   imports: [RouterOutlet, FileUploadComponent], // Import RouterOutlet and FileUploadComponent
// //   templateUrl: './app.component.html',
// // })
// // export class AppComponent {}



// import { Component } from '@angular/core';
// import { RouterOutlet } from '@angular/router';
// import { FileUploadComponent } from './file-upload/file-upload.component';

// @Component({
//   selector: 'app-root',
//   standalone: true,
//   imports: [RouterOutlet, FileUploadComponent], // Import necessary components
//   templateUrl: './app.component.html',
// })
// export class AppComponent {
//   title = 'Upload Image'; // Define title to fix the error
  
// }


import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FileUploadComponent } from './file-upload/file-upload.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, FileUploadComponent], // Import necessary components
  templateUrl: './app.component.html',
})
export class AppComponent {
  title = 'Animal Detection'; // Define title
}
