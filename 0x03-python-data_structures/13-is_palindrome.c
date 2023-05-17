#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of sinly linked list
 *
 * Return: returns 1 if true or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int *arr, index = 0, count, last_index;
	listint_t *current = *head;

	if ((head == NULL) || (*head == NULL))
		return (1);
	if (current->next == NULL)
		return (0);
	arr = (int *) malloc(1 * sizeof(int));
	if (arr == NULL)
		exit(EXIT_FAILURE);
	while (current != NULL)
	{
		arr[index] = current->n;
		if (current->next != NULL)
		{
			index++;
			arr = (int *) realloc(arr, (index + 1) * sizeof(int));
			if (arr == NULL)
				exit(EXIT_FAILURE);
		}
		current = current->next;
	}
	last_index = index;
	for (count = 0; count < ((index + 1) / 2); count++)
	{
		if (arr[count] != arr[last_index])
		{
			free(arr);
			return (0);
		}
		last_index--;
	}
	free(arr);
	return (1);
}
