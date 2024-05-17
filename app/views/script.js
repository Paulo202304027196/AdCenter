<script>
  $(document).ready(function() {
    $('tbody tr').click(function() {
      window.location.href = $(this).find('td a').attr('href');
    });
  });
</script>