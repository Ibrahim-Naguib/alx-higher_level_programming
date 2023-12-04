#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to a pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (is_pal(head, *head));
}

/**
 * is_pal - check if a sublist is a palindrome.
 * @start: A pointer to a pointer to the start of the sublist.
 * @end: A pointer to the end of the sublist.
 *
 * Return: 1 if the sublist is a palindrome, 0 otherwise.
 */

int is_pal(listint_t **start, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (is_pal(start, end->next) && (*start)->n == end->n)
	{
		*start = (*start)->next;
		return (1);
	}
	return (0);
}
