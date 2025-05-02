export async function fetchDateTime() {
    try {
        const response = await fetch('/datetime');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.text();
        return data;
    } catch (error) {
        console.error('Error fetching date and time:', error);
        throw error;
    }
}