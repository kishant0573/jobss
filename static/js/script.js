// Example data
const applicants = [
    { name: 'John Doe', position: 'Software Engineer', email: 'john@example.com', pdf: 'john_resume.pdf' },
    { name: 'Jane Smith', position: 'Web Developer', email: 'jane@example.com', pdf: 'jane_resume.pdf' },
    // Add more applicants here
  ];
  
  // Function to populate applicant table
  function populateApplicantTable() {
    const tableBody = document.getElementById('applicantTableBody');
    tableBody.innerHTML = '';
  
    applicants.forEach(applicant => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${applicant.name}</td>
        <td>${applicant.position}</td>
        <td>${applicant.email}</td>
        <td><a href="${applicant.pdf}" target="_blank">Download</a></td>
      `;
      tableBody.appendChild(row);
    });
  }
  
  // Function to update number of applications
  function updateNumApplications() {
    const numApplications = applicants.length;
    document.getElementById('numApplications').textContent = numApplications;
  }
  
  // Generate PDF report (dummy function)
  function generatePDFReport() {
    // Your PDF generation logic here
    alert('PDF report generated successfully!');
  }
  
  // Populate initial data
  populateApplicantTable();
  updateNumApplications();
  
  // Event listener for generating PDF report button
  document.getElementById('generateReportBtn').addEventListener('click', generatePDFReport);
  