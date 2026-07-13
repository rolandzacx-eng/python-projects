#include<stdio.h>
#include<stdlib.h>

// Function to perform insertion sort on an array
void insertion_sort(int array[], int n) {
    int i, j, key;
    
    // Start from the second element (index 1) because the first element (index 0)
    // is considered already sorted initially
    for (i = 1; i < n; i++) {
        // The element to be placed in the sorted part
        key = array[i];
        
        // j points to the last element of the sorted part
        j = i - 1;
        
        // Shift elements of the sorted part that are greater than 'key'
        // to one position ahead of their current position
        while (j >= 0 && array[j] > key) {
            array[j + 1] = array[j];
            j = j - 1;
        }
        
        // Place the key in its correct position
        array[j + 1] = key;
    }
}

int main() {
    int n, i;
    
    // Read the number of items
    printf("Enter the number of items: ");
    scanf("%d", &n);
    
    // Handle empty input case
    if (n <= 0) {
        printf("No items to sort.\n");
        return 0;
    }
    
    // Dynamically allocate memory for the array
    int *array = (int*)malloc(n * sizeof(int));
    if (array == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    
    // Read the numbers from standard input
    printf("Enter %d numbers: ", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }
    
    // Sort the array using insertion sort
    insertion_sort(array, n);
    
    // Print the sorted array
    printf("Sorted array: ");
    for (i = 0; i < n; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
    
    // Free allocated memory
    free(array);
    
    return 0;
}

