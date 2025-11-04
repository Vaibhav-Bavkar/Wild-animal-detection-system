import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common'; // Ensure CommonModule is imported

@Component({
  selector: 'app-file-upload',
  standalone: true, // If using standalone components
  imports: [CommonModule], // Ensure CommonModule is included
  templateUrl: './file-upload.component.html',
  styleUrls: ['./file-upload.component.css']
})
export class FileUploadComponent {
  selectedFile: File | null = null;
  previewImage: string | ArrayBuffer | null = null;
  isUploading = false;
  uploadSuccess = false;
  predictedAnimal: string | null = null;

  constructor(private http: HttpClient) {}

  onFileSelected(event: Event) {
    const fileInput = event.target as HTMLInputElement;
    if (fileInput.files && fileInput.files.length > 0) {
      this.selectedFile = fileInput.files[0];

      const reader = new FileReader();
      reader.onload = (e) => {
        this.previewImage = e.target?.result as string | ArrayBuffer;
      };
      reader.readAsDataURL(this.selectedFile);
    }
  }

  onDragOver(event: DragEvent) {
    event.preventDefault();
  }

  onDrop(event: DragEvent) {
    event.preventDefault();
    if (event.dataTransfer?.files.length) {
      this.selectedFile = event.dataTransfer.files[0];

      const reader = new FileReader();
      reader.onload = (e) => {
        this.previewImage = e.target?.result as string | ArrayBuffer;
      };
      reader.readAsDataURL(this.selectedFile);
    }
  }

  removeSelectedImage() {
    this.selectedFile = null;
    this.previewImage = null;
  }

  uploadFile() {
    if (!this.selectedFile) {
      return;
    }

    const formData = new FormData();
    formData.append("image", this.selectedFile);

    this.isUploading = true;
    this.uploadSuccess = false;
    this.predictedAnimal = null;

    this.http.post<{ animal: string }>('http://127.0.0.1:5000/predict', formData)
      .subscribe(
        (response) => {
          this.predictedAnimal = response.animal;
          this.uploadSuccess = true;
          this.isUploading = false;
        },
        (error) => {
          console.error('Error uploading file:', error);
          this.isUploading = false;
        }
      );
  }

  uploadAnother() {
    this.selectedFile = null;
    this.previewImage = null;
    this.uploadSuccess = false;
    this.predictedAnimal = null;
  }
}
