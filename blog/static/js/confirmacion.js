function confirmareliminacion(id) {
  Swal.fire({
    title: 'Are you sure?',
    text: "You won't be able to revert this!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete it!',
    cancenButtonText:'Cancelar'
  }).then((result) => {
    if (result.value) {
      window.location.href= `/eliminar/${id}/`;
    
    }
  })
}

function editarelemento(id){
  Swal.fire({
    title: 'Are you sure?',
    text: "Desea Editar el Elemneto ",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, Edit',
    cancenButtonText:'Cancelar'
  }).then((result) => {
    if (result.value) {
      window.location.href= `/modificar/${id}/`;
    
    }
  })

}

function agregarnuevo(){
  Swal.fire({
    title: 'Custom animation with Animate.css',
    showClass: {
      popup: 'animate__animated animate__fadeInDown'
    },
    hideClass: {
      popup: 'animate__animated animate__fadeOutUp'
    },
    timer:5000,
  })
}

function modificar2(){
  Swal.fire({
    position: 'top-end',
    icon: 'success',
    title: 'Your work has been saved',
    showConfirmButton: false,
    timer: 6500
  })
}



