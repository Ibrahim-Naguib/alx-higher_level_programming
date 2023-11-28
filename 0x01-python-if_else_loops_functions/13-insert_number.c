#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - Inserts a new node with a given number into a sorted list.
 * @head: A pointer to a pointer to the head of the sorted linked list.
 * @number: The value to insert into the sorted list.
 *
 * Return: A pointer to the new node, or NULL on failure.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *temp = *head;

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (temp == NULL || new->n < temp->n)
	{
		new->next = temp;
		*head = new;
		return (new);
	}

	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;

	new->next = temp->next;
	temp->next = new;

	return (new);
}
