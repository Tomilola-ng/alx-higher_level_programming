#include <stdio.h>
#include <Python.h>

/**
 * print_info_bytes - Prints bytes information
 *
 * @obj: Python Object
 * Return: void
 */
void print_info_bytes(PyObject *obj)
{
	char *str;
	long int len, i, max;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	len = ((PyVarObject *)(obj))->ob_size;
	str = ((PyBytesObject *)obj)->ob_sval;

	printf("  size: %ld\n", len);
	printf("  trying string: %s\n", str);

	max = len >= 10 ? 10 : len + 1;

	printf("  first %ld bytes:", max);

	for (i = 0; i < max; i++)
		printf(" %02x", str[i] < 0 ? 256 + str[i] : str[i]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_info_float - Prints float information
 *
 * @obj: Python Object
 * Return: void
 */
void print_info_float(PyObject *obj)
{
	double val;
	char *num;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(obj))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	val = ((PyFloatObject *)(obj))->ob_fval;
	num = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", num);
	setbuf(stdout, NULL);
}

/**
 * print_info_list - Prints list information
 *
 * @obj: Python Object
 * Return: void
 */
void print_info_list(PyObject *obj)
{
	long int len, i;
	PyListObject *lst;
	PyObject *item;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(obj))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	len = ((PyVarObject *)(obj))->ob_size;
	lst = (PyListObject *)obj;

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", lst->allocated);

	for (i = 0; i < len; i++)
	{
		item = lst->ob_item[i];
		printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);

		if (PyBytes_Check(item))
			print_info_bytes(item);
		if (PyFloat_Check(item))
			print_info_float(item);
	}
	setbuf(stdout, NULL);
}
