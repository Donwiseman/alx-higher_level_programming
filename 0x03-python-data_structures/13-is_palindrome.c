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
	int *int_arr[], index;

	if ((head == NULL) || (*head == NULL))
		return (1);
	if (*head->next == NULL)
		return (0)
}
