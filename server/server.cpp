#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <regex>
#include <sstream>
#include <unordered_map>

std::vector<std::string> split (const std::string &s, char delim) {
    std::vector<std::string> result;
    std::stringstream ss (s);
    std::string item;

    while (std::getline (ss, item, delim)) {
        result.push_back (item);
    }

    return result;
}

std::vector<std::string> getColumnsFromSchema(const std::string &tableName){
	
	std::string line;
	
	std::ifstream myfile(tableName + "/schema");
	std::getline (myfile,line);
	
	auto columns = split(line,',');
	myfile.close();

	return columns;
}

int getData(std::string tableName, std::vector<std::string> columnlist, std::vector<std::string> &dataBuffer){
	
	// Get column names from schema
	// Create hash table for column names
	auto columns = getColumnsFromSchema(tableName);
	std::unordered_map <std::string, int > columnMap;
	int k = 0;
	for(auto col: columns)
		columnMap[col] = k++;

	bool needAllCols = false;
	if(columnlist.size() == 1 && columnlist[0].compare("*") == 0)
		needAllCols = true;

	// open data file
	std::ifstream myfile(tableName + "/data");
	
	// check if file opened
	if(!myfile.is_open()){
		return -1;
	}

	std::string line, resultline;

	// start reading
	while ( std::getline (myfile,line) ){
			
		// all cols required. 
		// just push to result
		if(needAllCols)
			dataBuffer.push_back(line);
		
		// selective cols needed.
		// columnMap holds col number of each col name
		// columnlist holds required col names
		// resultline = ""
		// 1. split the line into data vector 
		// 2. for each col in columnlist, get the col num from columnMap
		else{
			resultline = "";
			auto dataVector = split(line, ',');
			for(auto col : columnlist ){
				int colnum = columnMap[col];
				resultline = resultline + dataVector[colnum] + ",";
			}
			resultline.pop_back();
			dataBuffer.push_back(resultline);

		}

    }

    myfile.close();
    

	return 0;
}

std::vector<std::string> parseSQL(std::string inputstr){
	
	auto pos = inputstr.find(" from ");
	std::string columns = inputstr.substr(7, pos-7);
	auto columnlist = split(columns,',');
	return columnlist;
}

int main(){

	std::string inputstr;
	
	while(1){
		std::cout << "SQL>";
		std::getline(std::cin, inputstr);
	
		if(inputstr.compare("exit")==0)
			break;

		std::regex sqlformat("(select )(.*)( from )(.*)(;)");
		if( !std::regex_match(inputstr,sqlformat)) {
        	std::cout << "Invalid query" << std::endl;
        	continue;
		}

		auto columnlist = parseSQL(inputstr);
		
		std::vector<std::string> dataBuffer;
		getData("emp",columnlist, dataBuffer);

		for(std::string s : dataBuffer)
			std::cout << s << std::endl;

    }
	
	return 0;
}