exports.formatDate = currentDate => {
    // Get the day, month, year, hours, and minutes
    const day = currentDate.getDate().toString().padStart(2, '0');
    const month = (currentDate.getMonth() + 1).toString().padStart(2, '0'); // Note: January is 0
    const year = currentDate.getFullYear().toString();
    const hours = currentDate.getHours().toString().padStart(2, '0');
    const minutes = currentDate.getMinutes().toString().padStart(2, '0');

    // Format the date and time
    const formattedDateTime = `${day}/${month}/${year} ${hours}:${minutes}`;
    return formattedDateTime
}