#include "Python.h"
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	int len = 0, a;
	char *s;
	PyBytesObject *py_c = (PyBytesObject *) p;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(py_c))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
	else
	{
		len = PyBytes_Size(p);
		printf("  size: %d\n", len);
		printf("  trying string: %s\n", py_c->ob_sval);
		s = py_c->ob_sval;
		if ((len + 1) >= 10)
			a = 10;
		printf("  first %d bytes: ", a);
		while (a--)
			printf(" %.2x", (unsigned char) *s++);
		printf("\n");
	}
}
void print_python_list(PyObject *p)
{
	int i;
	long long len;
	PyListObject *py_c = (PyListObject *) p;
	PyObject *it;

	len = (long long) PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lld\n", len);
	printf("[*] Allocated = %lld\n", (long long) py_c->allocated);
	for (i = 0; i < len; ++i)
	{
		it = PyList_GET_ITEM(p, i);
		printf("Element %lld: %s\n", i, it->ob_type->tp_name);
		if (PyBytes_Check(it))
			print_python_bytes(it);
	}
}
