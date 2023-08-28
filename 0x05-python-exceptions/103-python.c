#include <stdio.h>
#include "Python.h"


void print_python_bytes(PyObject *p)
{
	Py_ssize_t len = ((PyVarObject *)(p))->ob_size, len2;
	char *s;
	PyBytesObject *py_c = (PyBytesObject *) p;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(py_c))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	else
	{
		/*len = PyBytes_Size(p);*/
		printf("  size: %ld\n", len);
		s = py_c->ob_sval;
		printf("  trying string: %s\n", s);
		len2 = len + 1;
		if (len2 >= 10)
			len2 = 10;
		printf("  first %ld bytes: ", len2);
		/*while (len2--)
		*	printf("%02x ", (unsigned char) *s++);
		*/
		printf("\n");
	}
}
void print_python_float(PyObject *p)
{
	double d;
	char *s;
	PyFloatObject *py_c = (PyFloatObject *) p;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_Check(py_c))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	d =  py_c->ob_fval;
	s = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", s);
}
void print_python_list(PyObject *p)
{
	Py_ssize_t  len = ((PyVarObject *)(p))->ob_size, i;
	PyListObject *py_c = (PyListObject *) p;
	PyObject *it;

	/*len = PyList_GET_SIZE(p);*/
	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %lu\n", py_c->allocated);
	for (i = 0; i < len; ++i)
	{
		it = py_c->ob_item[i];
		printf("Element %ld: %s\n", i, it->ob_type->tp_name);
		if (PyBytes_Check(it))
			print_python_bytes(it);
		if (PyFloat_Check(it))
			print_python_float(it);
	}
}
