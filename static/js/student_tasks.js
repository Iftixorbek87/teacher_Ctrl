document.addEventListener('DOMContentLoaded', function() {
    const taskItems = document.querySelectorAll('.task-item');
    
    taskItems.forEach(item => {
        item.addEventListener('click', async function() {
            const taskNumber = this.getAttribute('title').replace('Vazifa #', '');
            const studentId = this.closest('.student-container')?.dataset.studentId || '{{ student.id }}';
            const taskElement = this;
            
            try {
                const response = await fetch('/students/toggle-task/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    body: JSON.stringify({
                        student_id: studentId,
                        task_number: parseInt(taskNumber)
                    })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    // Toggle the completed class
                    taskElement.classList.toggle('completed');
                    
                    // Update the task status icon
                    const statusElement = taskElement.querySelector('.task-status');
                    if (data.completed) {
                        statusElement.innerHTML = `
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="20 6 9 17 4 12"></polyline>
                            </svg>
                        `;
                    } else {
                        statusElement.innerHTML = '<div class="task-pending"></div>';
                    }
                    
                    // Update the progress bar
                    const progressBar = document.querySelector('.progress-bar-fill');
                    if (progressBar) {
                        progressBar.style.width = data.progress + '%';
                        
                        // Update progress text if it exists
                        const progressText = document.querySelector('.progress-text');
                        if (progressText) {
                            progressText.textContent = data.progress + '% bajarildi';
                        }
                        
                        // Update completed count if it exists
                        const completedCount = document.querySelector('.completed-count');
                        if (completedCount) {
                            completedCount.textContent = data.completed_count;
                        }
                        
                        // Show/hide completion message
                        const completionMessage = document.querySelector('.completion-message');
                        if (data.is_graduated && !completionMessage) {
                            const message = document.createElement('div');
                            message.className = 'completion-message';
                            message.style.color = 'var(--success)';
                            message.style.fontWeight = '700';
                            message.style.marginTop = '0.5rem';
                            message.style.fontSize = '0.9rem';
                            message.textContent = '🏆 Barcha vazifalarni bajardi!';
                            progressBar.parentElement.parentElement.appendChild(message);
                        } else if (!data.is_graduated && completionMessage) {
                            completionMessage.remove();
                        }
                    }
                } else {
                    console.error('Error toggling task:', data.error);
                    alert('Xatolik yuz berdi. Iltimos, qaytadan urinib ko\'ring.');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Xatolik yuz berdi. Iltimos, qaytadan urinib ko\'ring.');
            }
        });
    });
});

// Helper function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
